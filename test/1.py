import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from markdownify import MarkdownConverter

url = "https://thecorestandards.org/Math/Content/1/OA/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find(class_="article-header")
title = title.find("h1").get_text()

# print(title)

sidebar = soup.find(id="sidebar")
hrefs = [a['href'] for a in sidebar.find_all('a', href=True)]
print(hrefs)

article = soup.find('article')
if article:
    # article_html = md(str(article), strip=['a'])
    article_text = MarkdownConverter().convert_soup(article)
    # print(response.text)
    # print(response)

    # with open("article_content.md", "w", encoding="utf-8") as file:
    #     file.write(article_html)
    # print("内容已成功写入article_content.txt")
