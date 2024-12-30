import re

# 示例字符串
url = "https://www.thecorestandards.org/Math/Content/1/OA/"

# 使用正则表达式提取'Math'
match = re.search(r'org/(.*?)/', url)

if match:
    extracted = match.group(1)  # 获取匹配的部分
    print("提取的部分:", extracted)
else:
    print("没有找到匹配的部分。")