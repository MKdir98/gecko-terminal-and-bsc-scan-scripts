from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import traceback
import pytz
import time

goodWallets = {
    '0x60eb78f048a0879eba2f2e1e10c66574bf0fbee6': {},
    '0x665a389866246adabb6c35a9bdf9b11466ed7aba': {},
    '0xa34c0cce57cd034c223fd3c45c33c2ccdfd75666': {},
    '0x9d4d7c9aad9b2c4b57705c82312ced50dd7f12ad': {},
    '0xf4cf01792eed87610b133551f61cc9d09194ef2a': {},
    '0xc06409851aa6b6c73831b58b7c636e766815c1ec': {},
    '0x25e9915ae49560b1c3c0ada1c65fab6ad2c4071d': {},
    '0x6bd6dfc7685462c0abbab0ea404c257bd8ef85fb': {},
    '0xabba1e279517aaeefafddd3a881fef6a7256a927': {},
    '0xb0053e87bf17aa9f6d1cd4c839764dd43f6cfc85': {},
    '0xe6edafacc09cf0a4721e820a82bc0c16831c4e86': {},
    '0x29a25eba7771b34362d543088d01d6a5d320d8cf': {},
    '0x5829575cb691c5c45c4579640e37066215ea369f': {},
    '0x447ef84cf779f22b5f4a1e91b478d0e8f9cac388': {},
    '0x478c7605099b0e4655c4224c541ab1a6e7e2c432': {},
    '0xb3d7e4cf4f98548a90b7434246b8130d3a7ae022': {},
    '0x1899edf409370fd8aa47a7b65b70a260596f13da': {},
    '0x2f875d925a1f9a62fa728d5785c106722e9bc1b3': {}
}

goodCoin = [
    '0xd8c0d3632c652ba5e1b24033a78cd25c286deccc',
    '0xdd7d785f91bba104c15080f288ec02c04817fa66',

]

scamWallets = {
    '0xf634ffc03299e58d0fada2e54b6b68d07935ee9d': {},
    '0x7afcf4894e25067be135369ac81b003f3bbea979': {},
    '0xe35571577f078d3cb38781dc4de094743821dac9': {},
    '0x650c12d9fe7779a2d494679be4e8d5953230d6af': {},
    '0x1885a9f11f99df0b3b66cb4afeaca806db502893': {},
    '0x76a4d1e319851390e9a190688e8801f27a588f88': {},
    '0x769543d5026d0d26650973615930c5585d8b329a': {},
    '0x5e1665148c58711fcf4f688788468940c51d6bab': {},
    '0x02ecf21a29c43738f0f676aa5e8e85db9835c981': {},
    '0xf7514638d921ff923da842937b23a548c7cafd00': {},
    '0xd0a6a9a54c2070c516c4866667a0a4b0f2b51e7f': {},
    '0x1131e02a4f8e8feb3726072b579c76c30c4812f8': {},
    '0x916b5c772738813c553f849f59a7f544d1b8f29b': {},
    '0x5b4846f5850e9035898a196faf5ae92e608d3a8b': {},
    '0x585603c04f1ee70d0771b1d172115f4211584b84': {},
    '0x0657a2f78d5a6d1abf74d347ec377d166a56aec4': {},
    '0xb00b197bfd1c7264103be82ee244d0a9518781f2': {},
    '0xa54952c8409e55f18328eed6ddc7c06b34d4a1f9': {},
    '0x29315b7029eae8bbc2323b416387db2743c1b5b7': {},
    '0x602624e4d2535c9822c0be01a3ca6f2849cf8dc7': {},
    '0xbd38c47348f7d107528b0a8a5837ab0913625478': {},
    '0x599974bb9982cd185cdb5adf7e64e352eec4d1cd': {},
    '0xb824cfa5146c309c30f0c9db9e07e1778758217b': {},
    '0xd46e4f00cc459db4e4458f1e7040b56205fcfe66': {},
    '0xca40620fd385c45008636375f5f63c5aee0420de': {},
    '0x0acfdc16bd5d455e1f635d1f342df3c45455e5c0': {},
    '0x07eda203967c3790cd44514f83be24ce15074bfe': {},
    '0xb78f3af9a59d6b63c8c452c5e31de78ed8317eab': {},
    '0x538ac74d9501d864d091b8377dc891a76d28801d': {},
    '0x296670198b66396016d2c2dd8f9e08ff1f6122ad': {},
    '0x64a43e4c51b9654895cd8d7c57444d4bc6427fb8': {},
    '0xca5c3d466b17c0ed28c7967e957131ebfb0dd5b7': {},
    '0x856bd140cb12ba738451b926cc2f0bbb694ed306': {},
    '0x9d7e302c5f9e827904678fac07f389566d236924': {},
    '0xb469f292c546925c8826e188bdf50588f4029005': {},
    '0x16869327a7aa323166ff881a07e6e1a152e9dfd7': {},
    '0x296670198b66396016d2c2dd8f9e08ff1f6122ad': {},
    '0x85da20e9760ef193531c3b0a9a2bd5abf60bff21': {},
    '0x856bd140cb12ba738451b926cc2f0bbb694ed306': {},
    '0xcdefad9e464873f21a162db4a86aa73d4ca89470': {},
    '0xa114d918e516c2c4e042b819230a84b7d0860c0f': {},
    '0x599974bb9982cd185cdb5adf7e64e352eec4d1cd': {},
    '0x75365a99ebd3efca80812cbb3d1e3022c81ee093': {},
    '0xd46e4f00cc459db4e4458f1e7040b56205fcfe66': {},
    '0xbb592cde1215e89779b2ebb08cde522121ec41a3': {},
    '0xc67255f6860e9d9b424a9dc21b68dbf30501a0d6': {}
}


def pretty(address, trxs):
    result = "```"+address + "```"
    for trx in trxs:
        for x, y in trx.items():
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
    if time_difference > timedelta(minutes=2):
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


def getLastTransactions(address):
    url = "https://bscscan.com/tokentxns?a=" + address
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
    for row in rows:
        tds = row.find_all('td')
        if len(tds) == 0:
            continue
        data = {}
        if tds[6].find('a') != None:
            if tds[6].find('a').get('data-clipboard-text') != None:
                data['from'] = tds[6].find('a').get('data-clipboard-text')
            else:
                data['from'] = tds[6].find('a').get('data-bs-title')
        else:
            data['from'] = tds[6].text

        if tds[8].find('a') != None:
            if tds[8].find('a').get('data-clipboard-text') != None:
                data['to'] = tds[8].find('a').get('data-clipboard-text')
            else:
                data['to'] = tds[8].find('a').get('data-bs-title')
        else:
            data['to'] = tds[8].text

        data['tx'] = tds[1].find('a').get('href').split('/')[2]
        data['method'] = tds[2].find('span').get('title')
        data['time'] = tds[3].text
        data['value'] = tds[9].find('span').get('data-bs-title')
        data['token'] = tds[10].find('a').get(
            'href').split('?')[0].split('/')[2]
        goodWallets[address][data['tx']] = data
    result = []
    for y in goodWallets[address].values():
        if check_time_difference(y['time']):
            result.append(y)
    goodWallets[address] = {}
    return result


def waitForScamsComing(address):
    url = "https://bscscan.com/tokentxns?a=" + address
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
    for row in rows:
        tds = row.find_all('td')
        if len(tds) == 0:
            continue
        data = {}
        if tds[6].find('a') != None:
            if tds[6].find('a').get('data-clipboard-text') != None:
                data['from'] = tds[6].find('a').get('data-clipboard-text')
            else:
                data['from'] = tds[6].find('a').get('data-bs-title')
        else:
            data['from'] = tds[6].text

        if tds[8].find('a') != None:
            if tds[8].find('a').get('data-clipboard-text') != None:
                data['to'] = tds[8].find('a').get('data-clipboard-text')
            else:
                data['to'] = tds[8].find('a').get('data-bs-title')
        else:
            data['to'] = tds[8].text

        data['tx'] = tds[1].find('a').get('href').split('/')[2]
        data['method'] = tds[2].find('span').get('title')
        data['time'] = tds[3].text
        data['value'] = tds[9].find('span').get('data-bs-title')
        data['token'] = tds[10].find('a').get(
            'href').split('?')[0].split('/')[2]
        scamWallets[address][data['tx']] = data
    result = []
    tokens = []
    for y in scamWallets[address].values():
        # if y['token'] not in tokens:
        #     tokens.append(y['token'])
        if check_time_difference(y['time']):
            if y['token'] not in tokens:
                result.append(y)
    scamWallets[address] = {}
    return result


while True:
    for scamWallet in scamWallets.keys():
        try:
            trs = waitForScamsComing(scamWallet)
            if len(trs) > 0:
                send_msg("scams are coming " + pretty(scamWallet, trs))
        except Exception as ex:
            print(traceback.format_exc())
    # for goodWallet in goodWallets.keys():
    #     try:
    #         trs = getLastTransactions(goodWallet)
    #         if len(trs) > 0:
    #             send_msg(pretty(goodWallet, trs))
    #     except Exception as ex:
    #         print(traceback.format_exc())
    time.sleep(70)
