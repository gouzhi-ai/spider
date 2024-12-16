#!/usr/bin/env Python
# -*- coding: utf-8 -*-



import requests

targetURL = "https://www.baidu.com/"

def get_proxy_ip():
    # 提取代理API接口，获取1个代理IP
    # api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=o20zlo0jk023m5a5kpcn&signature=mmc86y59mgjjf4vbuo1bkrwbok77xbyb&num=1&pt=1&sep=1"
    api_url ="https://share.proxy.qg.net/get?key=HY8XE52G&num=1&area=&isp=0&format=txt&seq=\r\n&distinct=false"
    # 获取API接口返回的代理IP
    proxy_ip = requests.get(api_url).text

    return proxy_ip
def get_proxy(proxyAddr):
    # 用户名密码认证(私密代理/独享代理)
    # proxyAddr = "您的代理IP:端口"
    # proxyAddr=get_proxy_ip()
    authKey = "HY8XE52G"
    password = "CAB2A8E85455"
    # 账密模式
    proxyUrl = "http://%(user)s:%(password)s@%(server)s" % {
        "user": authKey,
        "password": password,
        "server": proxyAddr,
    }
    proxies = {
        "http": proxyUrl,
        "https": proxyUrl,
    }
    return proxies

# resp = requests.get(targetURL, proxies=get_proxy(get_proxy_ip()))
# print(resp.content.decode('utf-8'))


#
#
# def get_proxy(proxy_ip):
#     # 用户名密码认证(私密代理/独享代理)
#     username = "d2458418424"
#     password = "383bbzzl"
#     proxies = {
#         "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
#         "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
#     }
#
#     return proxies

