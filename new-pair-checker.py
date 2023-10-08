import json
import time
from datetime import datetime, timedelta
import requests
import traceback
import pytz


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


def expired(date_string):
    given_date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    current_date = datetime.now()
    time_difference = current_date - given_date
    if time_difference > timedelta(days=2):
        return True
    else:
        return False


def findGroup(pairAddress, networkIdentifier):
    swaps = json.loads(requests.request('GET', 'https://app.geckoterminal.com/api/p1/' + networkIdentifier + '/pools/' + pairAddress +
                                        '/swaps?include=from_token%2Cto_token').text)
    gangs = json.loads(open('scams-gangs-' + networkIdentifier + '.json', 'r').read())

    for swap in swaps['data']:
        for gang, addresses in gangs.items():
            if swap['attributes']['tx_from_address'] in addresses:
                pair['gang'] = gang
                send_msg(gang + ' start to attack ' + pretty(pair))
                return gang
    return None


pairs = json.loads(open('new-pairs').read())
open('new-good-pairs', 'a+')
data = open('new-good-pairs', 'r').read()
config = json.loads(open('config.json', 'r').read())
if data == '':
    data = '{}'
newGoodPairs = json.loads(data)

for pair in list(pairs):
    if pair in newGoodPairs.keys():
        value = newGoodPairs[pair]
    else:
        value = pairs[pair]
    if 'gang' in value.keys():
        continue
    networkIdentifier = value['networkIdentifier']
    pairData = json.loads(requests.request("GET", 'https://app.geckoterminal.com/api/p1/' + networkIdentifier + '/pools/' + pair +
                                           '?include=dex%2Cdex.network.explorers%2Cnetwork_link_services%2Ctoken_link_services%2Cdex_link_services%2Cpairs&base_token=0').text)
    totalLiquidity = pairData['data']['attributes']['reserve_in_usd']
    value['liquidity'] = totalLiquidity
    if float(totalLiquidity) > 10000 and pair not in newGoodPairs.keys():
        send_msg(pretty(value))
    newGoodPairs[pair] = value

for address in list(newGoodPairs):
    if 'gang' in newGoodPairs[address].keys():
        continue
    group = findGroup(address, newGoodPairs[address]['networkIdentifier'])
    if group != None:
        send_msg("grabage " + address)
        newGoodPairs[address]['gang'] = group

for address in list(newGoodPairs):
    if expired(newGoodPairs[address]['time']) and float(newGoodPairs[address]['liquidity']) < 10000 and 'gang' not in newGoodPairs[address].keys():
        newGoodPairs.pop(address)

json.dump(newGoodPairs, open('new-good-pairs', 'w+'))
