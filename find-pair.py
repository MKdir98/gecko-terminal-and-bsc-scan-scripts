import requests
import re
from bs4 import BeautifulSoup
import json
import traceback


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


open('pairs', 'a+')

data = open('pairs', 'r').read()
if data == '':
    data = '{}'

pairs = json.loads(data)

url = "https://bscscan.com/address/0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"

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

url = "https://bscscan.com/address-events?m=light&a=0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73&v=0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73&sid=" + sid

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

response = requests.request("GET", url, headers=headers, data=payload)
soup = BeautifulSoup(response.text)
trs = soup.find('tbody').find_all('tr', recursive=False)
for tr in trs:
    tds = tr.find_all('td', recursive=False)
    txHash = tds[0].text
    if txHash in pairs.keys():
        continue
    time = tds[2].text
    method = tds[5].text
    detail = tds[6].find_all(attrs={'class': 'text-monospace'})[2].find_all(
        attrs={'style': 'display: inline-block; height: 25px;'})
    pair1Address = detail[0].text
    pair2Address = detail[1].text
    pair = detail[2].text
    quantity = detail[3].text
    value = {'txHash': txHash, 'time': time,
             'method': method, 'pair1Address': pair1Address,
             'pair2Address': pair2Address, 'pair': pair,
             'quantity': quantity}
    send_msg(pretty(value))
    if pair not in pairs.keys():
        pairs[pair] = value

json.dump(pairs, open('pairs', 'w+'))
