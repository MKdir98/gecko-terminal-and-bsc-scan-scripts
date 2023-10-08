import requests
# from bs4 import BeautifulSoup

# def getEcoLink(geckoLink):
#     url = "https://www.coingecko.com" + geckoLink

#     payload={}
#     headers = {
#     'authority': 'www.coingecko.com',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
#     'cache-control': 'max-age=0',
#     'cookie': '_gaexp=GAX1.2.wdQfiN-rQT6nmgQxbaKaCA.19672.0; indexCategoryCardTrend=true; _session_id=72f7b4e815a69a776371ebd799dc2f1d; _gcl_au=1.1.1120448316.1692634419; _au_1d=AU1D-0100-001692634421-I3L8ON5L-14MM; _gid=GA1.2.1778809171.1692634422; _cc_id=57f4c5515d82a5de72744252046bbb87; panoramaId_expiry=1693246449721; panoramaId=000d64e1f96c95fee983ec421a994945a702bd7df81abaa468266493cc4fbe32; panoramaIdType=panoIndiv; hideAddCoinModal=true; cookie_notice_accept=1; _au_last_seen_pixels=eyJhcG4iOjE2OTI3MjU5ODQsInR0ZCI6MTY5MjcyNTk4NCwicHViIjoxNjkyNzI1OTg0LCJydWIiOjE2OTI3MjU5ODQsInRhcGFkIjoxNjkyNzI1OTg0LCJhZHgiOjE2OTI3MjU5ODQsImdvbyI6MTY5MjcyNTk4NCwiaW5kZXgiOjE2OTI3MjU5ODQsImltcHIiOjE2OTI3MjYwNDEsImNvbG9zc3VzIjoxNjkyNzI2MDQxLCJzbWFydCI6MTY5MjcyNjA0MSwidGFib29sYSI6MTY5MjcyNjA0MSwic29uIjoxNjkyNzI2MDQxLCJiZWVzIjoxNjkyNzI1OTg0LCJvcGVueCI6MTY5MjcyNjA0MSwicHBudCI6MTY5MjcyNjA0MSwiYWRvIjoxNjkyNzI2MDQxLCJ1bnJ1bHkiOjE2OTI3MjYwNDEsImFtbyI6MTY5MjcyNTk4NH0%3D; geckoTableFdvStats=true; __cf_bm=WT0iPwMKscJLSVtNr3Bbngyb.sRpTiKM_tE4Fp_LAck-1692728006-0-AbhcXz5h9MzvTqz207yKnuh3nkk96b4ZChHFVu7BefVWbP2PDIn4ES5Z3wrZoge0jNec49FOVHiazHxoX4sACBo=; __gads=ID=6b09fc5ce218ef39:T=1692634339:RT=1692728013:S=ALNI_MZAIqMGm3OH8DCc46-uXKROxU9ReQ; __gpi=UID=00000c64c9fce8d4:T=1692634339:RT=1692728013:S=ALNI_MayBBA6S7_X89LDH-Nm2RqTOeA5AQ; _ga_LJR3232ZPB=GS1.1.1692725977.4.1.1692728148.0.0.0; _ga=GA1.2.2090155246.1692634419; datadome=0YFOKDOJfclfZu6~NUKf2tItlqdPo~u26QfHSUYRHQU-nc5y~ImP3CEcjgDu1bEHokV5s23SgjJNG7~28JBp~CnKpjQ8T7IOcX~JPURm3~W5iFGvN70IYpyMh728lnFl',
#     'referer': 'https://www.coingecko.com/en/crypto-gainers-losers',
#     'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
#     }

#     response = requests.request("GET", url, headers=headers, data=payload)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     link = soup.find('a').get('href')
#     return link


# url = "https://www.coingecko.com/en/crypto-gainers-losers"

# payload={}
# headers = {
#   'authority': 'www.coingecko.com',
#   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#   'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
#   'cache-control': 'max-age=0',
#   'cookie': '_gaexp=GAX1.2.wdQfiN-rQT6nmgQxbaKaCA.19672.0; geckoTableFdvStats=false; indexCategoryCardTrend=true; _session_id=72f7b4e815a69a776371ebd799dc2f1d; _gcl_au=1.1.1120448316.1692634419; _au_1d=AU1D-0100-001692634421-I3L8ON5L-14MM; _gid=GA1.2.1778809171.1692634422; _cc_id=57f4c5515d82a5de72744252046bbb87; panoramaId_expiry=1693246449721; panoramaId=000d64e1f96c95fee983ec421a994945a702bd7df81abaa468266493cc4fbe32; panoramaIdType=panoIndiv; hideAddCoinModal=true; __cf_bm=5lJfz4QDD5LzfYlPEatTBcFA9VmXD4eMeaIHG78Hof0-1692725893-0-AarjwvMHLN/DxnGbD24PqthQZ9HAIoXodSQvoq/ERwNll45vOBzXhGo0Q8WlkK3tPXpMgkZITMnCVfyYDGNb+lk=; __gads=ID=6b09fc5ce218ef39:T=1692634339:RT=1692725901:S=ALNI_MZAIqMGm3OH8DCc46-uXKROxU9ReQ; __gpi=UID=00000c64c9fce8d4:T=1692634339:RT=1692725901:S=ALNI_MayBBA6S7_X89LDH-Nm2RqTOeA5AQ; cookie_notice_accept=1; _au_last_seen_pixels=eyJhcG4iOjE2OTI3MjU5ODQsInR0ZCI6MTY5MjcyNTk4NCwicHViIjoxNjkyNzI1OTg0LCJydWIiOjE2OTI3MjU5ODQsInRhcGFkIjoxNjkyNzI1OTg0LCJhZHgiOjE2OTI3MjU5ODQsImdvbyI6MTY5MjcyNTk4NCwiaW5kZXgiOjE2OTI3MjU5ODQsImltcHIiOjE2OTI3MjYwNDEsImNvbG9zc3VzIjoxNjkyNzI2MDQxLCJzbWFydCI6MTY5MjcyNjA0MSwidGFib29sYSI6MTY5MjcyNjA0MSwic29uIjoxNjkyNzI2MDQxLCJiZWVzIjoxNjkyNzI1OTg0LCJvcGVueCI6MTY5MjcyNjA0MSwicHBudCI6MTY5MjcyNjA0MSwiYWRvIjoxNjkyNzI2MDQxLCJ1bnJ1bHkiOjE2OTI3MjYwNDEsImFtbyI6MTY5MjcyNTk4NH0%3D; _ga_LJR3232ZPB=GS1.1.1692725977.4.1.1692726082.0.0.0; _ga=GA1.2.2090155246.1692634419; datadome=3Tl1l6y5~6hH00AylCA8ez1fZ4~7nEV3ka_~alx4A9SNEOsZaj1wwOZEAyIRu_Sztz2cVdTfyJCrksqy9ikA-0qbQn6yrr_o0rKwGFVP~mHQWlOct7ZGLJjUTrG1jtpf',
#   'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Linux"',
#   'sec-fetch-dest': 'document',
#   'sec-fetch-mode': 'navigate',
#   'sec-fetch-site': 'none',
#   'sec-fetch-user': '?1',
#   'upgrade-insecure-requests': '1',
#   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# soup = BeautifulSoup(response.text, 'html.parser')
# tds = soup.select('.tw-flex-1.tw-mb-6 td.py-0.coin-name.cg-sticky-col.cg-sticky-third-col.px-0')
# links = [td.find('a').get('href') for td in tds]
# for link in links:
#     print(getEcoLink(link))

import json
import re
from datetime import datetime
import traceback
import time

def getGoodCoins(dex):
    coins = []
    endPageNumber = None
    pageNumber = 1
    while(True):
        try:
            url = "https://app.geckoterminal.com/api/p1/bsc/pools?" +\
                "dex=" + dex + "&" +\
                "include=dex%2Cdex.dex_metric%2Cdex.network%2Ctokens" +\
                "&page=" + str(pageNumber) +\
                "&include_network_metrics=true"
            response = requests.request("GET", url)
            result = json.loads(response.text)
            if endPageNumber == None:
                endPageNumber = int(re.search(r'page=(\d+)', result['links']['last']['href']).group(1))
            for row in result['data']:
                liq = float(row['attributes']['reserve_in_usd'])
                changePercent = float(row['attributes']['price_percent_changes']['last_24h'][:-1])
                name = row['attributes']['name']
                address = row['attributes']['address']
                vol = float(row['attributes']['to_volume_in_usd'])
                if float(changePercent) < -98 and vol > 10000 and 'WBNB' in name:
                    coins.append([changePercent, name, address])
            if pageNumber == endPageNumber:
                break
            pageNumber = pageNumber + 1
        except Exception as ex:
            print(traceback.format_exc())

    return coins

def timeIsFor24Ago(time):
    date = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
    time_diff = datetime.utcnow() - date
    return time_diff.days == 0 and time_diff.seconds < 86400

def getLuckyWallets(address, changePercent):
    firstPrice = None
    luckyWallet = []
    findLastDate = False
    pageNumber = 1
    endPageNumber = None
    while True:
        try:
            if findLastDate or endPageNumber == pageNumber:
                break
            url = "https://app.geckoterminal.com/api/p1/bsc/pools/"\
                + address + "/swaps?include=from_token%2Cto_token&page=" + str(pageNumber)
            response = requests.request("GET", url)
            result = json.loads(response.text)
            if endPageNumber == None:
                endPageNumber = int(re.search(r'page=(\d+)', result['links']['last']['href']).group(1))
            for row in result['data']:
                type = row['attributes']['price_from_in_currency_token']
                price = float(row['attributes']['price_to_in_usd'])
                time = row['attributes']['timestamp']
                if firstPrice == None:
                    firstPrice = price
                    # middlePrice = firstPrice / (1 + (changePercent * 0.5 / 100))
                totalPrice = float(row['attributes']['to_token_total_in_usd'])
                # if price < middlePrice:
                    # if row['attributes']['tx_from_address'] not in [x[0] for x in luckyWallet]:
                if totalPrice > 500:
                    luckyWallet.append([row['attributes']['tx_from_address'], time, type, totalPrice])
                if not timeIsFor24Ago(time):
                    findLastDate = True
                    break
            pageNumber = pageNumber + 1
        except Exception as ex:
            print(traceback.format_exc())

    return luckyWallet

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

send_msg('follow whales')
allDetails = {}
coins =  getGoodCoins('pancakeswap-v3-bsc') + getGoodCoins('pancakeswap_v2')
    
print(str(coins))
send_msg(str(coins))
# for coin in coins:
#     addresses = getLuckyWallets(coin[2], coin[0])
#     allDetails[coin[1]] = addresses
#     send_msg(coin[1] + " addresses: " + str(addresses))

# print(allDetails)
