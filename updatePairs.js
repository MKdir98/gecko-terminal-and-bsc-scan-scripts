const db = require("./db");
const { Web3 } = require('web3');
const web3 = new Web3(new Web3.providers.HttpProvider("https://bsc-dataseed.binance.org/"))
const fs = require('fs')
const axios = require('axios');
const { parse } = require('node-html-parser');


async function getTax(pair) {
    var config = {
        method: 'get',
        url: 'https://www.geckoterminal.com/bsc/pools/' + pair,
        headers: {
            'authority': 'www.geckoterminal.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': '__qca=I0-1775320373-1694276767427; ahoy_visitor=8aa5fd3f-c3bb-4f8a-bd9c-aba8298784dc; _uc_referrer=https://www.coingecko.com/; _uc_utm_source=coingecko; _uc_utm_medium=referral; _uc_utm_term=; _uc_utm_content=; _pbjs_userid_consent_data=3524755945110770; _uc_utm_campaign=livechart-btn; _ga_X7G8VKSH3M=deleted; _ga=GA1.1.595499950.1692634998; _ga_X7G8VKSH3M=deleted; ahoy_visit=aea2e83d-c380-45b8-b00c-b5ee42110c76; __gads=ID=bbdd30191bd2eebf:T=1692634924:RT=1695840843:S=ALNI_MbTLVFhv_y2tn-oBbnxIyhW8deiYQ; __gpi=UID=00000c64ca6d84be:T=1692634924:RT=1695840844:S=ALNI_MbZE9Y-T6yT2Jtav3daPzSR6xFCgw; ahoy_events=%5B%5D; mp_604ec6861e5a709347ca3e3807a92e0f_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18a18e862e8eee-09447daa1b9359-17462c6c-1fa400-18a18e862e9eef%22%2C%22%24device_id%22%3A%20%2218a18e862e8eee-09447daa1b9359-17462c6c-1fa400-18a18e862e9eef%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22initial_utm_source%22%3A%20%22coingecko%22%2C%22initial_utm_medium%22%3A%20%22referral%22%2C%22initial_utm_campaign%22%3A%20%22livechart-btn%22%2C%22initial_utm_content%22%3A%20null%2C%22initial_utm_term%22%3A%20null%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22utm_source%22%3A%20%22coingecko%22%2C%22utm_medium%22%3A%20%22referral%22%2C%22utm_campaign%22%3A%20%22livechart-btn%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.coingecko.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.coingecko.com%22%2C%22%24search_engine%22%3A%20%22google%22%7D; amp_2d2f38=of3HgJMVFBCJgekFsT7Lbr...1hbbvh8b3.1hbbvv09n.6v.0.6v; _ga_X7G8VKSH3M=GS1.1.1695840510.147.1.1695840961.0.0.0',
            'referer': 'https://www.geckoterminal.com/bsc/pancakeswap-v3-bsc/pools',
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
    var html = await axios(config);
    var buyTaxElement = parse(html.data).querySelector('.flex .flex-col .gap-2  .pr-3').firstChild.nextSibling;
    var sellTaxElement = buyTaxElement.nextSibling;
    var data = [Number(buyTaxElement.text.substring(8, buyTaxElement.text.length - 1)), Number(sellTaxElement.text.substring(9, sellTaxElement.text.length - 1))];
    return data;
}


async function update() {
    while (true) {
        try {
            db.each(`SELECT * FROM pairs`, async (error, row) => {
                try {
                    if (error) {
                        throw new Error(error.message);
                    }
                    factoryAddress = null;
                    if (row['pair_address'] == null) {
                        var factory = new web3.eth.Contract(JSON.parse(fs.readFileSync('factory.json', 'utf-8')), row['factory_address']);
                        var pairAddress = await factory.methods.getPair(row['token0'], row['token1']).call();
                        db.run(
                            `UPDATE pairs SET pair_address=? WHERE router_address=? and token0=? and token1=?`,
                            [pairAddress, row['router_address'], row['token0'], row['token1']],
                            function (error) {
                                if (error) {
                                    console.error(error.message);
                                }
                            }
                        );
                    } else if (row['buy_tax'] == null || row['sell_tax'] == null) {                        var tax = await getTax(row['pair_address']);
                        console.log(tax[0]);
                        console.log(tax[1]);
                        db.run(
                            `UPDATE pairs SET buy_tax=?, sell_tax=? WHERE router_address=? and token0=? and token1=?`,
                            [tax[0], tax[1], row['router_address'], row['token0'], row['token1']],
                            function (error) {
                                if (error) {
                                    console.error(error.message);
                                }
                            }
                        );
                    }
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
// getTax('0x8bdf24267648ceda929db2776eddf6b60b99d23a');