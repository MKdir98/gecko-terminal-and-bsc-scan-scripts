import json
from datetime import datetime, timedelta
import requests
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


gangsPair = json.loads(open('gangs-pair', 'r').read())
pairs = json.loads(open('pairs', 'r').read())

withoutGangs = []
for pair, value in pairs.items():
    if 'status' in value.keys() and value['status'] == 'sent-telegram':
        if pair not in gangsPair.keys():
            withoutGangs.append(pair)

send_msg('without gangs ' + str(withoutGangs))