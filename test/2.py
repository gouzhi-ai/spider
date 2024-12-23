import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "cookie": "sy2.ampId=1e882409-0eeb-4343-b42a-352be2f1e1a4; sy2.lang_preference=en; _sharedID=31e179fb-dae9-4ae3-9069-e782ebc81dda; _sharedID_cst=zix7LPQsHA%3D%3D; _ga=GA1.1.193927462.1733733266; pbjs-unifiedid_cst=zix7LPQsHA%3D%3D; AMP_MKTG_68b292e677=JTdCJTdE; _cc_id=2f0f18740f975f215f044ec9d83db875; __gads=ID=e77b5454a77f69ed:T=1733733325:RT=1733736604:S=ALNI_MY_ywtYTjJ2uXwLbG5Pk8fO6wEyvg; __gpi=UID=00000f8811157821:T=1733733325:RT=1733736604:S=ALNI_MblNMxKOZsWT_UY8SAbtDtTUCs2SQ; __eoi=ID=c99d96884832bc26:T=1733733325:RT=1733736604:S=AA-AfjY4ihkcHag4Xalxy_1dP0aP; pbjs-unifiedid=%7B%22TDID%22%3A%2225550ca6-da80-499e-b497-b604b9683a81%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222024-12-09T09%3A31%3A36%22%7D; cto_bundle=_xmgU180UEtsdU5jOUp2RXVwakNRZUslMkJ4JTJCVHU2a0RZdzRNSDdZQTVZMFZETDlQbHlYMXdJaTB6Q255Y3IwRTh1UCUyRlJrQ1F3eTFxRllkQjBqZjBVS1dpdnVYQ3d1UFZ6RTFWWldtSEtxdlFhV09JaHNWdUR6NlQxZEphaCUyQm5sOWV6WHZn; cto_bundle=_xmgU180UEtsdU5jOUp2RXVwakNRZUslMkJ4JTJCVHU2a0RZdzRNSDdZQTVZMFZETDlQbHlYMXdJaTB6Q255Y3IwRTh1UCUyRlJrQ1F3eTFxRllkQjBqZjBVS1dpdnVYQ3d1UFZ6RTFWWldtSEtxdlFhV09JaHNWdUR6NlQxZEphaCUyQm5sOWV6WHZn; cto_bidid=Ia1dGV9WTFhYQTRZa2IxUGMxN1VhUTQ4NkV5bnphRmNYcEYlMkJJVXdOZ1o0JTJCS2YxM1h0bHk2NTVLRVBBZzRLejhyVHpCTkhsYUs2WGxURGU2NExub1lJdWlsNWclM0QlM0Q; cto_bundle=t9LeAl80UEtsdU5jOUp2RXVwakNRZUslMkJ4JTJCWVo0b1RrWkFEZHdHVyUyRnZUJTJGMUNER0xEMlNvZ3JyYjBrNENNaTllQmJvcUdOc09MdnlWSFc3WGFiajlZYk51M2xBOCUyQno1T3VUdllIWDZ3QTU1dERod2xaRjNFWW4wSWgzWE1Da1RyODJJMDc; _clck=djhkdc%7C2%7Cfry%7C0%7C1804; sy2.variation=0; sy2.token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3d3dy5zeW1ib2xhYi5jb20iLCJ1ZGlkIjpudWxsLCJzdWJzY3JpYmVkIjpudWxsLCJleHAiOjE3MzUwMDQyNDR9.gMGwhDFeTqbya3CsJKUF4dt41XDR0I_mZukfNn0xEx0; sy2.lang=en; PLAY_LANG=en; PLAY_SESSION=cc4ed973e015e6645b93cc136e0e0ed47c3a7ac6-___ID=409d331e-7b82-400a-a3a9-c6379451be11; AMP_9ec2dedd4e=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJlMTEzZTIxNi0zYjE3LTQ1NzUtYjgxNy0zNzZhZjc2YzU1YWIlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzM0OTQwMzMyNzI5JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczNDk0MDM1MzEzMiUyQyUyMmxhc3RFdmVudElkJTIyJTNBMTE4JTJDJTIycGFnZUNvdW50ZXIlMjIlM0EwJTdE; sy.amp.session=1734939855788; sy.amp.device=d5065f7c-8561-4730-8120-519b5c556814; _clsk=wduq2j%7C1734940485374%7C9%7C1%7Cp.clarity.ms%2Fcollect; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Dec+23+2024+15%3A59%3A31+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202312.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false; AMP_68b292e677=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJkNTA2NWY3Yy04NTYxLTQ3MzAtODEyMC01MTliNWM1NTY4MTQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzM0OTM5ODU1Nzg4JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczNDk0MDc3MjEzMCU3RA==; _ga_X78WH5ZJPD=deleted",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.symbolab.com/popular-calculations",
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
url = "https://www.symbolab.com/popular-statistics"
response = requests.get(url, headers=headers)

print(response.text)
print(response)