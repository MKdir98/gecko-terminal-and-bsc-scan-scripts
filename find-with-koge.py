from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import traceback
import pytz
import json
import re

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


def getRows(p):

    url = "https://bscscan.com/address/0xe6df05ce8c8301223373cf5b969afcb1498c5528"

    payload = {}
    headers = {
        'authority': 'bscscan.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'ASP.NET_SessionId=y322lmctcxvzq3z4onmcy0xc; bitmedia_fid=eyJmaWQiOiI1MzRmZDQyNTE5MTAxMmFkYjEzODg4OGI4YjJiNWMxYyIsImZpZG5vdWEiOiI0NTE2NzliMzEwZmNmMDE5MWNkMTI0NzVjNzQyMzA2MCJ9; __stripe_mid=43e674ed-1e13-4e90-9339-731cc46545e1c7b59b; bscscan_cookieconsent=True; _ga_T1JC9RNQXV=deleted; _ga_T1JC9RNQXV=GS1.1.1692947544.13.0.1692947812.0.0.0; _ga=GA1.1.781513989.1692645415; _ga_5Q0CRCD3YN=GS1.1.1693664015.1.1.1693665401.0.0.0; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvMSxPzFY7Gm4G; _ga_PQY6J2Q8EP=deleted; cf_clearance=GDI4_lAjdwcM17w624BjisQ053wCiKyXsQkNNWKkFF8-1694170609-0-1-140ec119.cc3c0700.430f9ef9-0.2.1694170609; _ga_PQY6J2Q8EP=GS1.1.1694170581.14.1.1694172447.0.0.0; ASP.NET_SessionId=c3xp4xtiepzyo0e4h1jculqc; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvTHVtELqNu9Ak',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    html = response.text
    sid = re.search(r'sid = \'.*\'', html).group(0).split('\'')[1]
    url = "https://bscscan.com/token/generic-tokentxns2?contractAddress=0xe6df05ce8c8301223373cf5b969afcb1498c5528&mode=&sid=" + sid + "&m=light&p=" + p

    payload = {}
    headers = {
        'authority': 'bscscan.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': 'ASP.NET_SessionId=y322lmctcxvzq3z4onmcy0xc; bitmedia_fid=eyJmaWQiOiI1MzRmZDQyNTE5MTAxMmFkYjEzODg4OGI4YjJiNWMxYyIsImZpZG5vdWEiOiI0NTE2NzliMzEwZmNmMDE5MWNkMTI0NzVjNzQyMzA2MCJ9; __stripe_mid=43e674ed-1e13-4e90-9339-731cc46545e1c7b59b; bscscan_cookieconsent=True; _ga_T1JC9RNQXV=deleted; _ga_T1JC9RNQXV=GS1.1.1692947544.13.0.1692947812.0.0.0; _ga=GA1.1.781513989.1692645415; _ga_5Q0CRCD3YN=GS1.1.1693664015.1.1.1693665401.0.0.0; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvMSxPzFY7Gm4G; _ga_PQY6J2Q8EP=deleted; cf_clearance=GDI4_lAjdwcM17w624BjisQ053wCiKyXsQkNNWKkFF8-1694170609-0-1-140ec119.cc3c0700.430f9ef9-0.2.1694170609; _ga_PQY6J2Q8EP=GS1.1.1694170581.14.1.1694172921.0.0.0; ASP.NET_SessionId=c3xp4xtiepzyo0e4h1jculqc; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvTHVtELqNu9Ak',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table')
    rows = table.find_all('tr')
    rows.reverse()
    data = []
    for row in rows:
        tds = row.find_all('td')
        if len(tds) == 0:
            continue
        if tds[9] == '1':
            continue
        methodName = tds[2].text
        time = tds[3].text
        if tds[6].find('a') != None:
            if tds[6].find('a').get('data-clipboard-text') != None:
                src = tds[6].find('a').get('data-clipboard-text')
            else:
                src = tds[6].find('a').get('title')
        else:
            src = tds[6].text
        if tds[8].find('a') != None:
            if tds[8].find('a').get('data-clipboard-text') != None:
                dest = tds[8].find('a').get('data-clipboard-text')
            else:
                dest = tds[8].find('a').get('title')
        else:
            dest = tds[8].text

        data.append({
            'method': methodName,
            'time': time,
            'src': src,
            'dest': dest
        })
    return data


addresses = json.loads(open('scams-gangs-bsc.json', 'r').read())

rows = getRows("4") + getRows("3") + getRows("2") + getRows("1")
for row in rows:
    if row['method'] == '0xe2e35583':
        if row['dest'] not in addresses['koge']:
            addresses['koge'].append(row['dest'])
    elif row['method'] == 'Transfer':
        if row['src'] in addresses['koge']:
            addresses['koge'].remove(row['src'])

# send_msg(str(addresses['koge']))
json.dump(addresses, open('scams-gangs-bsc.json', 'w+'))
