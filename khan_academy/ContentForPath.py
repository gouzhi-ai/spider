#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/7 下午3:23
# @Author  : 苏玉恒
# @File    : ContentForPath.py
# @Software: PyCharm
import json
import requests


headers = {
    'accept': "*/*",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    'cache-control': "no-cache",
    'cookie': "browsing_session_id=_zh-hans_bsid_f3cd18c6-8c87-444c-8cc5-0e5b1ebf0001; _ga_19G17DJYEE=GS1.1.1736228315.22.1.1736232932.0.0.0; OptanonAlertBoxClosed=2025-01-07T06:55:47.038Z; LIS=zh; KAAS=ulTWf8j7bO3y-o8nLhHioA; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jan+07+2025+15:07:17+GMT+0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f2597303-7d88-4d1f-8194-42143c821f2b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=HK%3B&AwaitingReconsent=false; KAAL=$OAyajby37Ve4WP-Z9SNFVdKoKMwwnt43b03eh4vIh3k.~sppiwx$a2FpZF81ODA5MzI5NTU2MjM3MjI2MTEwMDE5Nzk2*; KAAC=$D2L8M0Q1iSoxb9hRZ-24h7At-_ms4hyW0UGIzdcC0IY.~sppiwx$a2FpZF81ODA5MzI5NTU2MjM3MjI2MTEwMDE5Nzk2*$a2FpZF81ODA5MzI5NTU2MjM3MjI2MTEwMDE5Nzk2!0!1~3; browsing_session_expiry=Tue, 07 Jan 2025 07:47:24 GMT",
    'pragma': "no-cache",
    'priority': "u=1, i",
    'referer': "https://zh.khanacademy.org/math/algebra2",
    'sec-ch-ua': "\\Microsoft",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "\\Windows",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    'x-ka-fkey': "1"
}
url = "https://zh.khanacademy.org/api/internal/graphql/ContentForPath"
params = {
    "fastly_cacheable": "persist_until_publish",
    "pcv": "28777b8f54f630af2e448bdc39f1a7fef7d86f4d",
    "hash": "3712657851",
    "variables": '{"path":"math/algebra2","countryCode":"HK","kaLocale":"zh-hans","clientPublishedContentVersion":"28777b8f54f630af2e448bdc39f1a7fef7d86f4d"}',
    "lang": "zh-hans"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)