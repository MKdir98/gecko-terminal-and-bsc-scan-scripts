import requests
import re
from bs4 import BeautifulSoup
import json
import traceback
from datetime import datetime, timedelta
import pytz

def expired(date_string):
    given_date = datetime.strptime(date_string,"%Y-%m-%dT%H:%M:%S.%fZ")
    current_date = datetime.now()
    time_difference = current_date - given_date
    if time_difference > timedelta(days=2):
        return True
    else:
        return False

def send_msg(text):
    try:
        token = ""
        chat_id = ""
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        if len(text) > 4096:
            for x in range(0, len(text), 4096):
                params = {
                    "parse_mode": "MarkdownV2",
                    "chat_id": chat_id,
                    "text": text[x:x+4096],
                }
                resp = requests.get(url, params=params)
        else:
            params = {
                "parse_mode": "MarkdownV2",
                "chat_id": chat_id,
                "text": text,
            }
            resp = requests.get(url, params=params)

        # Throw an exception if Telegram API fails
        resp.raise_for_status()
    except Exception as ex:
        print(traceback.format_exc())


def pretty(map):
    result = ""
    for x, y in map.items():
        result = result + x + ": ```" + y + "```"
    return result


def getDetail(includedData, type, id):
    for include in includedData:
        if include['id'] == id and include['type'] == type:
            return include


open('new-pairs', 'a+')
data = open('new-pairs', 'r').read()
config = json.loads(open('config.json', 'r').read())
if data == '':
    data = '{}'
pairs = json.loads(data)

url = "https://app.geckoterminal.com/api/p1/latest_pools?include=dex%2Cdex.network%2Cpool_metric%2Ctokens&page=1&include_network_metrics=true"
payload = {}
headers = {
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.geckoterminal.com/',
    'sec-ch-ua-mobile': '?0',
    'Authorization': 'undefined',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"'
}
response = requests.request("GET", url, headers=headers, data=payload)
result = json.loads(response.text)
includedData = result['included']
pools = result['data']
for pool in pools:
    address = pool['attributes']['address']
    if address in pairs.keys():
        continue
    name = pool['attributes']['name']
    poolCreateTime = pool['attributes']['pool_created_at']
    dexId = pool['relationships']['dex']['data']['id']
    dexDetail = getDetail(includedData, 'dex', dexId)
    dexName = dexDetail['attributes']['name']
    networkId = dexDetail['relationships']['network']['data']['id']
    networkDetail = getDetail(includedData, 'network', networkId)
    networkIdentifier = networkDetail['attributes']['identifier']
    if networkIdentifier not in config['networks'].keys():
        continue
    token1Id = pool['relationships']['tokens']['data'][0]['id']
    token1Detail = getDetail(includedData, 'token', token1Id)
    token1Address = token1Detail['attributes']['address']
    token1Name = token1Detail['attributes']['name']
    token1Symbol = token1Detail['attributes']['symbol']
    token2Id = pool['relationships']['tokens']['data'][1]['id']
    token2Detail = getDetail(includedData, 'token', token2Id)
    token2Address = token2Detail['attributes']['address']
    token2Name = token2Detail['attributes']['name']
    token2Symbol = token2Detail['attributes']['symbol']
    if token2Address != config['networks'][networkIdentifier]['weth-address']:
        continue
    pairs[address] = {
        "address": address,
        "name": name,
        "time": poolCreateTime,
        "dex": dexName,
        "token1Address": token1Address,
        "token1Name": token1Name,
        "token2Address": token2Address,
        "token2Name": token2Name,
        "networkIdentifier": networkIdentifier
    }
    # send_msg(pretty(pairs[address]))
    
for address in list(pairs):
    if expired(pairs[address]['time']):
        pairs.pop(address)

json.dump(pairs, open('new-pairs', 'w+'))
