from bs4 import BeautifulSoup
import json
import requests

response = requests.get("https://www.symbolab.com/popular-statistics/statistics-0")

html_content = response.text
# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 提取 JSON 数据
script_tag = soup.find('script', {'id': '__NUXT_DATA__'})
if script_tag:
    script_tag_string = str(script_tag.string)

    # 打印 JSON 数据以调试
    print("提取的 JSON 数据:", script_tag_string)

    try:
        one_qa_data = {
            'question': '',
            'answer': '',
            'explain': [],
            'url': '',
            'subject': ''
        }
        json_data = json.loads(script_tag_string, strict=False)
        data = []
        for i in json_data:
            if isinstance(i, str):
                data.append(i)
        json_data = data
        step = 0
        jump = 0
        one_qa_data['url'] = response.url
        one_qa_data['subject'] = one_qa_data['url'].split('/')[-1].split('-')[0]
        for i in range(len(json_data)):
            print(json_data[i])
            if jump == 1:
                jump = 0
                continue
            if 'Solver' in json_data[i]:
                jump = 1
            if '/practice/' in json_data[i] or 'Solver2' in json_data[i] or one_qa_data['subject'].lower() == json_data[
                i]:
                break
            if 'step' == json_data[i]:
                step = 1
                continue
            if step == 1:
                one_qa_data['explain'].append(json_data[i])

            if 'context' in json_data[i] and 'acceptedAnswer' in json_data[i]:
                one_qa_data['question'] = json_data[i - 2]
                one_qa_data['answer'] = json_data[i + 2]
        print(one_qa_data)
    except json.JSONDecodeError as e:
        print("JSON 解析错误:", e)
else:
    print("未找到包含问题和答案的 JSON 数据。")
