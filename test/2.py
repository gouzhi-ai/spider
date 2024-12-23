#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/20 下午4:17
# @Author  : 苏玉恒
# @File    : 2.py
# @Software: PyCharm

import json



script_tag = """[
    "{\n  \"@context\": \"https://schema.org\",\n  \"@type\": \"FAQPage\",\n  \"mainEntity\": [\n  {\n    \"@type\": \"Question\",\n    \"name\": \"What is 169^{-1/2} ?\",\n    \"acceptedAnswer\": {\n      \"@type\": \"Answer\",\n      \"text\": \"The solution to 169^{-1/2} is 1/13\"\n    }\n  }]\n}\n",
    "{\n  \"@context\": \"https://schema.org\",\n  \"@type\": \"BreadcrumbList\",\n  \"itemListElement\": [\n  {\n    \"@type\": \"ListItem\",\n    \"position\": 1,\n    \"name\": \"Popular Problems\",\n    \"item\": \"https://www.symbolab.com/popular-algebra\"\n  },\n  {\n    \"@type\": \"ListItem\",\n    \"position\": 2,\n    \"name\": \"problem\",\n    \"item\": \"https://www.symbolab.com/popular-algebra/algebra-106\"\n  }]\n}\n"
]"""
if script_tag:
    script_tag_string = str(script_tag)
    # script_tag_string = script_tag_string.replace("\"", '\\"')

    # 打印 JSON 数据以调试
    # print("提取的 JSON 数据:", script_tag_string)

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