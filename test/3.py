import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "cookie": "_ga=GA1.1.1323559991.1733383172; _ga_XBD2XMMDZB=GS1.1.1735278295.10.1.1735279463.0.0.0",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.thecorestandards.org/Math/",
    "sec-ch-ua": "\\Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\\Windows",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
url = "https://www.thecorestandards.org/Math/Content/NF/"
response = requests.get(url, headers=headers)

print(response.text)
print(response)