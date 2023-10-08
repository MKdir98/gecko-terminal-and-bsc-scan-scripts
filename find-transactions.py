import requests
from bs4 import BeautifulSoup
import traceback

lastBlockNumber = None
goodWallets = [
    '0xf3b0073e3a7f747c7a38b36b805247b222c302a3',
    '0x9cd6140c2de8af7595629bcca099497f0c28b2a9',
    '0x628a6fe299589b4b5a67d4b43ccdcb4821b3d80c',
    '0x25cd302e37a69d70a6ef645daea5a7de38c66e2a',
    '0x339b07af597a2c6128d067633611baf3f0725b1a',
    '0x16b2b042f15564bb8585259f535907f375bdc415',
    '0xaf2358e98683265cbd3a48509123d390ddf54534',
    '0x91ad1fa7f4fe58295028b09246587057762c2c19',
    '0x9d5db4b86afd9fe80720ca0f5637d6b790ce5bcb',
    '0x3a932fd72f2e01b3661401509493934fcae9652c',
    '0xc0b3218b16c2ec45df47422a18a5b1f6e070312f',
    '0x40c3fa73f2a3a0b5c70076254f9c5b5deab4bf7a',
    '0x3d8fc1cffaa110f7a7f9f8bc237b73d54c4abf61',
    '0x653d7e4998338677515a0edc0b97ada455a4efa0',
    '0x4a2c786651229175407d3a2d405d1998bcf40614',
    '0x26b17986128c21af763f97055680b36166402195',
]

def send_msg(text):
    try:
        text = '#test ' + text
        token = ""
        chat_id = ""
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        if len(text) > 4096:
            for x in range(0, len(text), 4096):
                params = {
                    "chat_id": chat_id,
                    "text": text[x:x+4096],
                }
                resp = requests.get(url, params=params)
        else:
            params = {
                "chat_id": chat_id,
                "text": text,
            }
            resp = requests.get(url, params=params)

        # Throw an exception if Telegram API fails
        resp.raise_for_status()
    except Exception as ex:
        print(traceback.format_exc())


def getLastTranactions():
    global lastBlockNumber
    url = "https://etherscan.io/txs"

    payload='__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ddlRecordsPerPage&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=SAoX9T1ORtRpcFneYAfmhqfTDCOL6aIJ4bdpimxB7Oc3aWtzBdDtQvG8qUMONaxOKUefs7oI1kl3oDzsJ5oobWk6EnyiifFu4tHXWPuerK4%3D&__VIEWSTATEGENERATOR=FCB51872&__EVENTVALIDATION=nCvuxvZgGioVkB0i9mSt7CfHxKkwmMXtKXLEtYoNML6xt3surSV46kXxhsIBZWzvGZwtwp7aP%2BbBpyUotBAnV3M%2Fg6r12GLUp6CCT1Y7dyN0zo0tNHC0kcUwjMTa%2FmDT06T6by%2FK44xV4jnC3oq8DxkvqyQfd0ooevsMIBVVTTWbm7%2BaBOwhQYO9ORw0JLDZDNDE%2FQSg7q164ewNuIQS%2FQ%3D%3D&ctl00%24ContentPlaceHolder1%24ddlRecordsPerPage=100'
    headers = {
    'authority': 'etherscan.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ASP.NET_SessionId=y322lmctcxvzq3z4onmcy0xc; _gid=GA1.2.518857024.1692645418; bitmedia_fid=eyJmaWQiOiI1MzRmZDQyNTE5MTAxMmFkYjEzODg4OGI4YjJiNWMxYyIsImZpZG5vdWEiOiI0NTE2NzliMzEwZmNmMDE5MWNkMTI0NzVjNzQyMzA2MCJ9; __stripe_mid=43e674ed-1e13-4e90-9339-731cc46545e1c7b59b; cf_clearance=XjsRgwBXI_7s.fhQQzwUXKbeJtJMS_3oDLtzJLHZm08-1692894080-0-1-f8cc96.26201b6.9bc9588f-0.2.1692894080; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvzRtTTAwXUid2; _ga_T1JC9RNQXV=deleted; _ga_T1JC9RNQXV=GS1.1.1692900359.11.1.1692908526.0.0.0; _ga=GA1.2.781513989.1692645415; _gat_gtag_UA_46998878_6=1; ASP.NET_SessionId=pi15fpopvdgf1nv5pu324d4r; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvNRwiiSPqLHwJ',
    'origin': 'https://etherscan.io',
    'referer': 'https://etherscan.io/txs',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table')
    rows = table.find_all('tr')
    dataRows = []
    for row in rows:
        tds = row.find_all('td')
        if len(tds) == 0:
            continue
        data = {}
        data['block'] = int(tds[3].text)
        if lastBlockNumber == None:
            lastBlockNumber = data['block']
        if data['block'] == lastBlockNumber:
            break
        data['tx'] = tds[1].find('a').get('href')
        data['method'] = tds[2].text
        data['from'] = tds[7].find('a').get('href')
        data['to'] = tds[9].find('a').get('href')
        dataRows.append(data)
    if len(dataRows) > 0:
        lastBlockNumber = dataRows[0]['block']
    return dataRows

while True:
    transactions = getLastTranactions()
    for transaction in transactions:
        if transaction['from'].split('/')[2] in goodWallets:
            send_msg(str(transaction))