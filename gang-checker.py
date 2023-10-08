import json
from datetime import datetime, timedelta
import requests
import traceback


def pretty(map):
    result = ""
    for x, y in map.items():
        result = result + x + ": ```" + y + "```"
    return result


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


def findGroup(pair):
    swaps = json.loads(requests.request('GET', 'https://app.geckoterminal.com/api/p1/bsc/pools/' + pair['pair'] +
                                        '/swaps?include=from_token%2Cto_token').text)
    gangs = json.loads(open('scams-gangs.json', 'r').read())

    for swap in swaps['data']:
        for gang, addresses in gangs.items():
            if swap['attributes']['tx_from_address'] in addresses:
                pair['gang'] = gang
                send_msg(gang + ' start to attack ' + pretty(pair))
                return gang
    return None


data = json.loads(open('pairs').read())
open('gangs-pair', 'a+')
gangsPair = open('gangs-pair', 'r').read()
if gangsPair == '':
    gangsPair = '{}'

gangsPair = json.loads(gangsPair)

for pair, value in data.items():
    if 'status' in value.keys() and value['status'] == 'sent-telegram' and  pair not in gangsPair.keys():
        gang = findGroup(data[pair])
        if gang != None:
            gangsPair[pair] = {
                'gang': gang,
                'time': value['time'],
                'pair': value['pair'],
                'pair1Address': value['pair1Address'],
                'pair2Address': value['pair2Address']
            }

json.dump(gangsPair, open('gangs-pair', 'w+'))
