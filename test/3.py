from bs4 import BeautifulSoup
import json
import requests
import re

response = requests.get("https://www.symbolab.com/popular-pre-algebra/pre-algebra-8")

html_content = response.text

item = {
    'question': 'BUG',
    'answer': 'BUG',
    'explain': [],
    'url': '',
    'subject': ''
}

item['url'] = response.url
item['subject'] = item['url'].split('/')[-1].rsplit('-', 1)[0]
# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')
script_tag = soup.find('div', class_= 'steps-container')
print(script_tag.get_text())
#
# # 提取 JSON 数据
# script_tag = soup.find('script', {'id': '__NUXT_DATA__'})
# json_data = json.loads(str(script_tag.string), strict=False)
#
# data = []
# for i in json_data:
#     if isinstance(i, str):
#         if i[0:7] == 'jypQO0p': continue
#         data.append(i)
# json_data = data
#
# # 求 question、answer
# question = 'BUG'
# answer = 'BUG'
# for i in range(len(json_data)):
#     # print(i)
#     if json_data[i] == 'interim':
#         if '=' in json_data[i + 1]:
#             question, answer = json_data[i + 1].split('=', 1)
#             if answer.count('$') % 4 != 0:
#                 question = question + "$$"
#                 answer = "$$" + answer
#         elif 'quad' in json_data[i + 1]:
#
#             pattern = r'(.*):.*?quad\}(.*)'
#
#             match = re.search(pattern, json_data[i + 1])
#
#             if match:
#                 question = match.group(1).strip()  # 获取冒号前的部分
#                 answer = match.group(2).strip()
#                 if answer.count('$') % 4 != 0:
#                     question = question + "$$"
#                     answer = "$$" + answer
#                     # print(question,answer)
#         break
#
# item['question'] = question
# item['answer'] = answer
#
# # 求 explain
# explain = []
# for i in range(len(json_data)):
#     # print(json_data[i])
#     if json_data[i] == 'step':
#         start = i+1
#         for j in range(start, len(json_data)):
#             if json_data[j] == item['subject']: break
#             explain.append(json_data[j])
#         break
#
# item['explain'] = explain
# print(json.dumps(item))
