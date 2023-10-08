const db = require("./db");
const { Web3 } = require('web3');
const web3 = new Web3(new Web3.providers.HttpProvider("https://bsc-dataseed.binance.org/"))
const fs = require('fs')
const axios = require('axios');
const { parse } = require('node-html-parser');


async function getPairsOfAPage(page) {
    var config = {
        method: 'get',
        url: 'https://bscscan.com/tokentxns?ps=100&p=' + page,
        headers: {
            'authority': 'bscscan.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': 'ASP.NET_SessionId=y322lmctcxvzq3z4onmcy0xc; bitmedia_fid=eyJmaWQiOiI1MzRmZDQyNTE5MTAxMmFkYjEzODg4OGI4YjJiNWMxYyIsImZpZG5vdWEiOiI0NTE2NzliMzEwZmNmMDE5MWNkMTI0NzVjNzQyMzA2MCJ9; __stripe_mid=43e674ed-1e13-4e90-9339-731cc46545e1c7b59b; bscscan_cookieconsent=True; _ga_T1JC9RNQXV=deleted; _ga_T1JC9RNQXV=GS1.1.1692947544.13.0.1692947812.0.0.0; _ga=GA1.1.781513989.1692645415; _ga_5Q0CRCD3YN=GS1.1.1693664015.1.1.1693665401.0.0.0; bscscan_switch_age_datetime=Age; _ga_PQY6J2Q8EP=GS1.1.1695497716.11.1.1695500788.0.0.0; bscscan_offset_datetime=+3.5; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvy3U61UwJSUHa; cf_clearance=v0Un2rOuCki2xO2ScYy5m5Eai8FoS2L0CA23KU0osq4-1695894076-0-1-a36c5b56.99a55791.900b0a21-0.2.1695894076; _ga_PQY6J2Q8EP=GS1.1.1695897350.22.1.1695900021.0.0.0',
            'referer': 'https://bscscan.com/tokentxns?ps=100&p=' + page,
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }
    };
    var tokensList = [];
    var html = await axios(config);
    var tableElement = parse(html.data).querySelector('table');
    var trElements = tableElement.querySelectorAll('tr');
    for (var trElement of trElements) {
        var tdElemetns = trElement.querySelectorAll('td');
        if (tdElemetns.length == 0) {
            continue;
        }
        var lastElement = tdElemetns[tdElemetns.length - 1];
        var token = lastElement.firstChild.getAttribute('href').split("/")[2];
        if (!tokensList.includes(token)) {
            tokensList.push(token);
        }
    }
    return tokensList;
}

function arrayToString(array) {
    let result = "(";
    for (let i = 0; i < array.length; i++) {
        result += "'" + array[i] + "'";
        if (i < array.length - 1) {
            result += ",";
        }
    }
    result += ")";
    return result;
}


async function getPairsOfAPages() {
    return (await getPairsOfAPage(1)).concat(await getPairsOfAPage(2));
}


async function update() {
    while (true) {
        try {
            var tokens = await getPairsOfAPages();
            db.each(`SELECT * FROM pairs where token1 in ` + arrayToString(tokens), async (error, row) => {
                try {
                    if (error) {
                        throw new Error(error.message);
                    }
                    var pair = new web3.eth.Contract(JSON.parse(fs.readFileSync('Pair.json', 'utf-8')), row['pair_address']);
                    var data = await pair.methods.getReserves().call();
                    if(row['token0'] > row['token1']) {
                        [data[0], data[1]] = [data[1], data[0]]
                    }
                    console.log(row['pair_address'] + " " + data)
                    db.run(
                        `UPDATE pairs SET reserve_in=?, reserve_out=? WHERE router_address=? and token0=? and token1=?`,
                        [data[0].toString(), data[1].toString(), row['router_address'], row['token0'], row['token1']],
                        function (error) {
                            if (error) {
                                console.error(error.message);
                            }
                        }
                    );
                } catch (ex) {
                    console.log(ex);
                }
            });
        } catch (ex) {
            console.log(ex);
        }
        await new Promise(resolve => setTimeout(resolve, 1000));
    }
}

update();