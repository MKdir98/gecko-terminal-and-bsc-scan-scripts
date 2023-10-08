import requests

url = "https://etherscan.io/advanced-filter?mtd=0x60806040%7e0x60806040&txntype=0"

payload={}
headers = {
  'authority': 'etherscan.io',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': 'ASP.NET_SessionId=qxrfpv3tbckggsbplu43sxib; bitmedia_fid=eyJmaWQiOiI1MzRmZDQyNTE5MTAxMmFkYjEzODg4OGI4YjJiNWMxYyIsImZpZG5vdWEiOiI0NTE2NzliMzEwZmNmMDE5MWNkMTI0NzVjNzQyMzA2MCJ9; __cuid=553a7bcdff0a4bc1b7c788ff443c264d; amp_fef1e8=43f889d1-24e0-40d0-8292-6b867c85150dR...1h9e89v88.1h9e89v8n.2.2.4; _ga_J9VZBWMCGL=GS1.1.1694003244.18.1.1694009348.0.0.0; _gid=GA1.2.450136076.1694635198; _ga_T1JC9RNQXV=deleted; __cflb=02DiuFnsSsHWYH8WqVXaqGvd6BSBaXQLUofm6bu4x17g8; __stripe_mid=f8337022-e0f7-4464-b6ae-f04d698c3ee0353a14; __stripe_sid=2f336f52-b40c-444c-848d-dfc6fa728c5def4f6e; cf_clearance=Bc_BnMlJlQSCaF8GSsASQdE5mXU0eCr_uDnKgAkgi34-1694718699-0-1-a61ac9f1.179256aa.f11b9611-150.2.1694717291; _gat_gtag_UA_46998878_6=1; _ga=GA1.2.1945313489.1692634783; _ga_T1JC9RNQXV=GS1.1.1694717289.45.1.1694718867.0.0.0',
  'referer': 'https://etherscan.io/advanced-filter?tadd=0x1a544aacb5e78214ea5145e49aef3ad65554071a&mtd=0x60806040%7e0x60806040&txntype=0',
  'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
