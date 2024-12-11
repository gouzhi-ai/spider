#!/usr/bin/env Python
# -*- coding: utf-8 -*-

"""
使用requests请求代理服务器
请求http和https网页均适用
"""

import requests


def get_proxy_ip():
    # 提取代理API接口，获取1个代理IP
    api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=o20zlo0jk023m5a5kpcn&signature=mmc86y59mgjjf4vbuo1bkrwbok77xbyb&num=1&pt=1&sep=1"

    # 获取API接口返回的代理IP
    proxy_ip = requests.get(api_url).text

    return proxy_ip


def get_proxy(proxy_ip):
    # 用户名密码认证(私密代理/独享代理)
    username = "d2458418424"
    password = "383bbzzl"
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
    }

    return proxies

# 白名单方式（需提前设置白名单）
# proxies = {
#     "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
#     "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
# }

# proxies = get_proxy()
#
# # 要访问的目标网页
# target_url = "https://dev.kdlapi.com/testproxy"
#
# # 使用代理IP发送请求
# response = requests.get(target_url, proxies=get_proxy(get_proxy_ip()))
#
# # 获取页面内容
# if response.status_code == 200:
#     print(response.text)
