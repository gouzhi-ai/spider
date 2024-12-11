# import requests
#
# headers = {
#     "Accept": "application/json, text/plain, */*",
#     "Accept-Language": "en;q=1,zh-CN,zh;q=0.9,fr;q=0.8",
#     "Agw-Js-Conv": "str",
#     "Cache-Control": "no-cache",
#     "Connection": "keep-alive",
#     "Content-Type": "application/json;charset=UTF-8",
#     "Cookie": "_region=cn; app_region=cn; _continent=as; _subdivision=2038349; _city=1816670;"
#               " device_id=7441861877418788408; ttwid=1%7CSfdHC_rKIJJxm5CGktDIiVAa8RFTIEAZejNVzLwqbkE%7C1732693507%7C81c86d1818d10c111cb383a88cbbe723adaf6c907d11de44233d16e37903a450;"
#               " _ga=GA1.1.198576221.1732693575; ak_bmsc=338E434F2D936C5B84FEB68C181E8897~000000000000000000000000000000~YAAQK2rRF6Hm2zGTAQAAqfNMixnhf4/W80emBEJR3KlVApuz/+An1c0EnjJHkHu1xHGpLdBdGGt8GJKCj1GBKTcDjWdw9lej6vx6xgQnAlZA3hyqT6TUtOFhu7mfqgLGOcap7BEB3rQ7qmzxw72csN2mDCklcs8pnuUJ8rjDv/2g1yetW6ft/fuUxHUu9t46MWtE+roYL5goCNNECI0SP06+cI+UKGlSUjjwQQN1a9LyNEzh8/xvUtB9ZI2ZBjHkJc2ruRCyVnVX06tR0WksvlF16Fp5Ox3sDx+kNAeh+CRyo29FpYXwloXJCItxsujab/uaBxwTyzOBXTt2LUYuO+P3MHTXSI7R3Au2XwZvEXSezmU88GOtQ13vcp9NnyacQP5zE/XCDkaW5hmYsvoeGR3bVSjOJafm6yTtFGFoqhvgXRR7vNVjTD5c/maoE+l4eWcuk4HYZkDABZ45BL6lkBE=; "
#               "_clck=s1fadj%7C2%7Cfre%7C0%7C1792; "
#               "_clsk=1przluk%7C1733208901958%7C2%7C0%7Ck.clarity.ms%2Fcollect; "
#               "bm_sv=7211DE1BA5C501FE6BA6A9ECADDB609E~YAAQxCMVAuNZfmaTAQAAMQhNixnqCX3OuseL4AiRR58j1QEobZmeBL8dpT43UbJEgN6B3wm0jV9LtMpEeyxh6K0mHgXrvbE+pxDTT6TxPvYvfPmB+Zvdgr0q3Nz+vVnWVqx3tJu/eXqYE2K7QsR8KzERv8MFogy+Up9/2j/6IrJRBmu9Aj39yAWYyXN9hwFTCaWR1WjDjLJ8yEs5k23oUPiWWs0jAHIEAL0E5MtvKCfAcjv2XN6ho3DmraU0p3ZEvX7p~1; "
#               "_ga_65B1F3RC9X=GS1.1.1733208896.3.1.1733208920.36.0.0",
#     "Origin": "https://www.gauthmath.com",
#     "Pragma": "no-cache",
#     "Referer": "https://www.gauthmath.com/",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-site",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
#     "X-Request-Source": "csr",
#     "sec-ch-ua": "\\Not)A;Brand;v=\\99, \\Microsoft",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\\Windows"
# }
# url = "https://api.gauthmath.com/ehi/web_api/question/list"
# params = {
#     "device_id": "7441861877418788408",
#     "aid": "369768",
#     "device_platform": "web",
#     "sub_platform": "web",
#     "_region": "cn",
#     "app_region": "cn",
#     "app_name": "ehi_overseas",
#     "language": "en",
#     "X-Valid-Requested": "true",
#     "msToken": "jfNO6OdQqiItdw4SD3eJY4qW_bxI6b8vdqfImEd13v87LzRMEoG3Se9TZP67K9rBfWN-HOYHXV17_jS_0kx9js7mgqqBr75svGQhpQyecgCvI1rLaR4V9lS-QMAoPPpa42iq0_Hzo6IQD7Mgtc6cGfyIEihenm4bwYygSRXxUAagoWllNA%3D%3D",
#     "a_bogus": "D7UfgFUjO2Accp%2FbmKONCf2RrIo%2FNBSytPT2WzUHSxquY7MczgeTi8TKGxqTbLVnbWs7%2FFl71jYAbnxYMjOZ1%2F9pKmpvuZUyAsVC9Wfo8qw3TMt0DrbBCLkzowBn0bTqe%2FVJiIU60UJHgjVAiqQY%2FB5y7KoKQbuBPZxSkZubx9shZM6AgZcrPBbswhVI"
# }
# data = {
#     "mode": "questions}}"
# }
# response = requests.post(url, headers=headers, params=params, data=data)
#
# print(response.text)
# print(response)

import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "cookie": "_region=cn; app_region=cn; _continent=as; _subdivision=2038349; _city=1816670; device_id=7441861877418788408; ttwid=1%7CSfdHC_rKIJJxm5CGktDIiVAa8RFTIEAZejNVzLwqbkE%7C1732693507%7C81c86d1818d10c111cb383a88cbbe723adaf6c907d11de44233d16e37903a450; _ga=GA1.1.198576221.1732693575; msToken=UP0EKwWdvGm7g43ieAN_PHa-gmuZua62n1FO7IUejg0bZ90yInNR7hW_glFS-1nO2a1jflZE1U2OudWHbUOx-_bJdDUJRY-Aao4Wrrn-qF415yFLV-gCpqhaaIiflbc45RneHP0=; gd_random_2234314=eyJtYXRjaCI6ZmFsc2UsInBlcmNlbnQiOjAuNzkxODYyMjcxMTU5NTEwOX0=.BdU+PbO3V7+yCIF8uA6VIzrl2Z6gJXrr7y4RrJHGUdw=; gd_random=eyJtYXRjaCI6dHJ1ZSwicGVyY2VudCI6MC4wNDUxODUzNzE2NzIwMTk0MTR9.S4dewkJhN6YPtGMk3/tABKiR8XTXy0jA75uPlbzTsQs=; _clck=s1fadj%7C2%7Cfre%7C0%7C1792; _clsk=1y5on7w%7C1733215324857%7C4%7C0%7Ck.clarity.ms%2Fcollect; ak_bmsc=7B698A4971F2E6105B845091EBF42B5B~000000000000000000000000000000~YAAQUXItFzo3p3mTAQAAFQ28ixkPhBEeGvEY8MYI5lY/cY0Ozalb+WVaxcNcl6s9T2r2zx3VTeQ3buKZ/0nqYMVnvMqnollEq2WTAn0A+uMcqoOrm/MlmK2dBYCDZv/tuF9ZDqpp7eAGhtlVD7n9PNpuyiqP+8T5xSu9T0IKdYjMVA0+MQnsHE/d1OgICi2kQJnizx27Qf9WzHsEod3bB/wvLQDuaNnj3p19MzCI5+mg3dsX7BopsGKqEkUq+wK8Y5y6BBGkL6CaW4Ejw7xKfuRDCX7JTkOFCYEP+GYC+mVlqD7ydcL9MgmgC9fsrF11y8XKhFfTIzr3F/Ht6BK0D+viZQaPcVqIoP7rn5WiAWQLVaTLCFD6AO10r0nWznHllUGpLHab87setC45PQScn2tjJbxuz+YkjvsJqU6KLTpempBooivx2poahknfJHI/1Perhu5cmF41yNFgIueiEGI=; __is_auto_resolve_trigger=; bm_sv=CD4729D891569D687BB76A5FD0D29140~YAAQDbIPF/LtKi+TAQAAXHnWixlSa+kLMi37FPrPlRrDBJlQPsj3e4ehrrqMsOMn0QYaHbdigXybYhUKvAsic2Ysw9l2icBEU5FgaqpZd6jnr4rtg9YA2BRsRNE/jQc1cevCIvAZTUbcPB1r0k8n61QypiQiTT1vndZ1u0BnBN+2POYnO6pC1xl9u5UERUFxhUnhAfIQX7spEXuXajz/kKQzjErRYLt5Zco8ec+7RjUz06m+FDGmfIWH/Tsxdj2K9fDA~1; _ga_65B1F3RC9X=GS1.1.1733216176.4.1.1733217918.29.0.0",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.gauthmath.com/study-resources/math/popular/3?mode=questions",
    "sec-ch-ua": "\\Not)A;Brand;v=\\99, \\Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\\Windows",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}
url = "https://www.gauthmath.com/solution/1814696913387573/280-Calcola-l-area-e-la-misura-del-contorno-della-parte-colorata-sapendo-che-il-"
response = requests.get(url, headers=headers)

print(response.text)
print(response)