
from bs4 import BeautifulSoup
import json
import requests


response =requests.get("https://www.symbolab.com/popular-algebra/algebra-106")

html_content=response.text
# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 提取 JSON 数据
script_tag = soup.find('script', {'id': '__NUXT_DATA__'})
if script_tag:
    script_tag_string = str(script_tag.string)

    # 打印 JSON 数据以调试
    print("提取的 JSON 数据:", script_tag_string)

    try:
        json_data = json.loads(script_tag_string, strict=False)

        # 提取问题、答案和步骤
        problem_latex = json_data[0][1]  # 问题的 LaTeX 格式
        solution_latex = json_data[1][1]  # 答案的 LaTeX 格式
        steps_latex = [step[1] for step in json_data[2][1]]  # 步骤的 LaTeX 格式

        # 输出结果
        print("问题的 LaTeX 格式:", problem_latex)
        print("答案的 LaTeX 格式:", solution_latex)
        print("步骤的 LaTeX 格式:")
        for step in steps_latex:
            print(step)
    except json.JSONDecodeError as e:
        print("JSON 解析错误:", e)
else:
    print("未找到包含问题和答案的 JSON 数据。")