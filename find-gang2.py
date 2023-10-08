from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import traceback
import pytz
import json

open('scams-tokens', 'a+')
data = open('scams-tokens', 'r').read()
if data == '':
    data = '{}'
scamsTransactions = json.loads(data)
addresses = json.loads(open('scams-gangs.json', 'r').read())


def pretty(map):
    result = ""
    for x, y in map.items():
        result = result + x + ": ```" + y + "```"
    return result


def check_time_difference(date_string):
    date_format = "%Y-%m-%d %H:%M:%S"
    given_date = datetime.strptime(date_string, date_format)
    given_date = pytz.utc.localize(given_date)  # تبدیل تاریخ به timezone UTC
    tehran_timezone = pytz.timezone('Asia/Tehran')  # تعریف timezone تهران
    given_date_tehran = given_date.astimezone(
        tehran_timezone)  # تبدیل تاریخ به timezone تهران
    # تعریف تاریخ فعلی با timezone تهران
    current_date = datetime.now(tz=tehran_timezone)
    time_difference = current_date - given_date_tehran
    if time_difference > timedelta(minutes=10):
        return False
    else:
        return True


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


def getWallets(address):
    url = "https://bscscan.com/txs?a=" + address
    payload = {}
    headers = {
        'authority': 'bscscan.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'ASP.NET_SessionId=qxrfpv3tbckggsbplu43sxib; bitmedia_fid=eyJmaWQiOiI1MzRmZDQyNTE5MTAxMmFkYjEzODg4OGI4YjJiNWMxYyIsImZpZG5vdWEiOiI0NTE2NzliMzEwZmNmMDE5MWNkMTI0NzVjNzQyMzA2MCJ9; _ga_T1JC9RNQXV=deleted; __cflb=02DiuFnsSsHWYH8WqVXcJWaecAw5gpnmefHrhpeTr91tg; _gid=GA1.2.103332998.1692970939; cf_clearance=ZdI_S0uEC_KjXkiu3js8Ij.GUiLJwu4BTrSiKofDfs4-1692970856-0-1-f8cc96.26201b6.9bc9588f-0.2.1692970856; _ga_T1JC9RNQXV=GS1.1.1692984940.8.1.1692984944.0.0.0; _ga=GA1.2.1945313489.1692634783',
        'referer': 'https://bscscan.com/address-tokenpage?m=light&a=' + address,
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

    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table')
    rows = table.find_all('tr')
    rows.reverse()
    data = []
    for row in rows:
        tds = row.find_all('td')
        if len(tds) == 0:
            continue
        if tds[9].find('a') != None:
            if tds[9].find('a').get('data-clipboard-text') != None:
                to = tds[9].find('a').get('data-clipboard-text')
            else:
                to = tds[9].find('a').get('data-bs-title')
        else:
            to = tds[9].text
        data.append(to)
    return data
  
wallets = getWallets("0x312d9cb02f690cbb86919fe56127539b22194ba8")
addresses = json.loads(open('scams-gangs.json', 'r').read())['group2']
excludedWallets = list(set([i for i in wallets if i not in addresses]))
if len(excludedWallets) != 0:
    send_msg(str(excludedWallets))
