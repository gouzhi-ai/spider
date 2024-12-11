import requests
from a_bogus import ABogus

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en;q=1,zh-CN,zh;q=0.9,fr;q=0.8",
    "Agw-Js-Conv": "str",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "_region=cn; app_region=cn; _continent=as; _subdivision=2038349; _city=1816670; device_id=7441861978060703288; ttwid=1%7CRyBG4M7jGpNWxvJDLrka2ns-QYgHStBasX8bkKRhcas%7C1732693528%7Cb70b1c38d333ce77c6467c39efc44c5d034ab90ed62996fbd6500a8d5dd080a8; _ga=GA1.1.1152745309.1732693532; _clck=1kg2f45%7C2%7Cfrg%7C0%7C1792; ak_bmsc=D38A9EB9CCE9482F49197215B5FE2A3E~000000000000000000000000000000~YAAQPiR+aER4GpOTAQAArSuElBrdAZSfDSqVFhnYShtza37z3sfXeh7dDzRXOtvpME9jw4fULfCBsgrbjBuOqKFgf0mkqrpNT3IWZwCi5TaXubDjiXLEOjrO46UAMnHb3grsknYWoY6SpDL8NxgN0BlMGegdd5kzWqCPu8B23Eo9LBORQ6xxpz9mGlVDE0ondA6t667fAInSeXp3M4MrKih/Qdkeiugd6YFK1XvmH3MQxFOhCSOoNbbr9ciK9gqK59w2Ky74u3eMtG4hsVPTQoVuPphjAJ1PVhbuLxlVC80pgZdt4eaWlMavAULWsFnMkKa4cBBtTjRPuj+n+kJObRzDjhXAGUvb/m+ZdimncU3QkfqVEL/ogCfnzMOI55Rf2Kvw80sEkAjQ9N32UYQ676prDV+azcuW9Y7CjOwmX3TKHOvvTZUYOj07DfaRaE3pZ4C5pyKjD+Rc6PWKoqhCduUX; _clsk=1iys145%7C1733363510843%7C1%7C0%7Ck.clarity.ms%2Fcollect; bm_sv=D686C20D410510920FAC03C56BEA79C2~YAAQPiR+aGZ4GpOTAQAAkzqElBrk5AMNafrWoIJtECgp9uDBztwzlsrSKkiXt0FiYlYaR5oLfLSjeUW6OaC84wmifhzzdHCDTPTDXwafycttFB0k2E5P9jxlOiFKOwgb1nIOfw+ywSS2saaXETJM4BZCINorcK1hzRp6+WRwr6ERlz+qQ00ONHi2ohIsfl87BKEKC+DUUYJA4+tpwT1C9RdurmoyZUbAM3JVH0PjnM927e2bWFMdeJOhphPqisCFRR7V~1; _ga_65B1F3RC9X=GS1.1.1733363509.7.0.1733363523.46.0.0",
    "Origin": "https://www.gauthmath.com",
    "Pragma": "no-cache",
    "Referer": "https://www.gauthmath.com/",
    "Host": "api.gauthmath.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "X-Request-Source": "csr",
    "sec-ch-ua": "\\Not)A;Brand;v=\\99, \\Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\\Windows"
}
url = "https://api.gauthmath.com/ehi/web_api/question/list"
params = {
    "device_id": "7444456011187144248",
    "aid": "369768",
    "device_platform": "web",
    "sub_platform": "web",
    "_region": "cn",
    "app_region": "cn",
    "app_name": "ehi_overseas",
    "language": "en",
    "X-Valid-Requested": "true",
    # "msToken": "sbyQrxiXHelmxdqTyMoVataQgnP4hJZ3YpNSqhUiBTkajA15oyUkuj6yxh_L--t8XGCki0VhWpY33OhZfFxmNXIYoQChy6ZOh5KL9Qz1Ag3XX6emgXpCmYJimVr0WxaOPaTgRpUl_Mj2Qzua_gRQF6J2BpuhlJXXBBpW09F_nS1xxhN03XnB6g^%^3D^%^3D",
    # "a_bogus": "dJ0VgzUyE2QRCpMt8KOPCVoRIKxArT8y8FidbGGHtPxhbXeOp6HikIE0GNNYboIfaSkXQe-HljF4bEfTBEE2XMHpwmkfSKsy4t^%^2FCnu8o8qZmbGihvNWPCvGxuiPT0CGY8^%^2FIni2R5Xs0K2EcWIH9wABI7o^%^2F3rm5EdPH-JVZunE9Km0WWjio^%^2Fna5jhiwwquD^%^3D^%^3D^"
}
data = {
    "Opt": {
        "SubjectKey": "Math",
        "KnowledgeKey": "",
        "Order": 1
    },
    "Page": 1,
    "PageSize": 10,
    "IsNeedVote": "true",
    "SharkParam": {
        "ReqFullPath": "https://www.gauthmath.com/study-resources/math/popular/1?mode=questions"
    }
}

bogus = ABogus(headers['User-Agent'])
a_bogus = bogus.generate_a_bogus(params)
print(a_bogus)
params['a_bogus'] = a_bogus

response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
print(response)

# Page
# :
# 1
# PageSize
# :
# 10
