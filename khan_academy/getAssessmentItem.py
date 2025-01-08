#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/7 上午10:26
# @Author  : 苏玉恒
# @File    : getAssessmentItem.py
# @Software: PyCharm

import json
import time
import datetime
import uuid
import requests

headers = {
    "authority": "zh.khanacademy.org",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "cookie": "gae_b_id=!$1bRN8CDPgNuHtJDSzTGoJi3DkMD9IssdMI-x26AstFc.~spi0ht~1$a2FpZF80MjU3Mzk5MjQ1MjEyMDE2NzQxMDcyMTU; OptanonAlertBoxClosed=2025-01-03T05:57:38.785Z; LIS=zh; KAAS=cUigHHTeT4oABeQZf7LQ2w; browsing_session_id=_zh-hans_bsid_68210190-a5ed-4d24-b6a3-9818c0c00001; _gcl_au=1.1.309757844.1736147154; _ga=GA1.1.662359369.1736147156; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jan+06+2025+15%3A41%3A32+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=ecb087ab-6e83-4216-93c5-42a00fa7563f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=US%3B&AwaitingReconsent=false; KAAL=$qgAOXqFP4D8VoiGcnHoPPNT20U0ocFHm7sznV4Jo-EU.~spnq0n$a2FpZF80MjU3Mzk5MjQ1MjEyMDE2NzQxMDcyMTU*; KAAC=$3jLfeNFBp0-4Un509MpDTMTa2dtLtb_xHMGALuzEL1U.~spnq0n$a2FpZF80MjU3Mzk5MjQ1MjEyMDE2NzQxMDcyMTU*$a2FpZF80MjU3Mzk5MjQ1MjEyMDE2NzQxMDcyMTU!0!1~3; _ga_19G17DJYEE=GS1.1.1736149284.2.1.1736150150.0.0.0; browsing_session_expiry=\\Mon,",
    "origin": "https://zh.khanacademy.org",
    "pragma": "no-cache",
    "referer": "https://zh.khanacademy.org/math/algebra2/manipulating-functions/function-composition/e/evaluate-composite-functions-from-formulas",
    "sec-ch-ua": "\\Chromium;v=\\122, \\Not(A:Brand;v=\\24, \\Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\\Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36",
    "x-ka-fkey": "1"
}
url = "https://zh.khanacademy.org/api/internal/graphql/getAssessmentItem"
params = {
    "lang": "zh-hans",
    # "_": "250102-0827-dab4161a87c1_1736150152776"
    "_": f"{int(datetime.datetime.now().timestamp())}-{uuid.uuid4()}"
}
exerciseId = "x9dd681f5"
itemId = "x99792e491eed798f"
query = "query getAssessmentItem($input: AssessmentItemInput!) {\n  assessmentItem(input: $input) {\n    item {\n      id\n      sha\n      problemType\n      itemData\n      __typename\n    }\n    error {\n      code\n      debugMessage\n      __typename\n    }\n    __typename\n  }\n}"
data_dict = {
    "operationName": "getAssessmentItem",
    "variables": {
        "input": {
            "exerciseId": exerciseId,
            "itemId": itemId
        }
    },
    "query": query
}

data = json.dumps(data_dict)
response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)
