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

def send_msg(text, isGang):
    try:
        if isGang:
            token = ""
        else:
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
    date_format = "%Y-%m-%d %H:%M:%S"
    given_date = datetime.strptime(date_string, date_format)
    given_date = pytz.utc.localize(given_date)  # تبدیل تاریخ به timezone UTC
    tehran_timezone = pytz.timezone('Asia/Tehran')  # تعریف timezone تهران
    given_date_tehran = given_date.astimezone(
        tehran_timezone)  # تبدیل تاریخ به timezone تهران
    # تعریف تاریخ فعلی با timezone تهران
    current_date = datetime.now(tz=tehran_timezone)
    time_difference = current_date - given_date_tehran
    if time_difference > timedelta(days=2):
        return True
    else:
        return False

data = json.loads(open('pairs').read())
for pair in list(data):
    value = data[pair]
    pairData = json.loads(requests.request("GET", 'https://app.geckoterminal.com/api/p1/bsc/pools/' + pair +
                                           '?include=dex%2Cdex.network.explorers%2Cnetwork_link_services%2Ctoken_link_services%2Cdex_link_services%2Cpairs&base_token=0').text)
    totalLiquidity = pairData['data']['attributes']['reserve_in_usd']
    data[pair]['liquidity'] = totalLiquidity
    if totalLiquidity == None:
        totalLiquidity = 0
    if 'status' not in list(data):
        data[pair]['status'] = ''
    if float(totalLiquidity) > 30000 and data[pair]['status'] != 'sent-telegram':
        send_msg('new good pair ' + pretty(data[pair]), False)
        data[pair]['status'] = 'sent-telegram'
    if expired(value['time']) and float(totalLiquidity) < 30000:
        data.pop(pair)


json.dump(data, open('pairs', 'w+'))
