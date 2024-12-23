from bs4 import BeautifulSoup
import json
import requests

response = requests.get("https://www.symbolab.com/popular-statistics")

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# links = soup.find_all('class_', 'solution-examples-page')
question_links = soup.find_all(class_='popular_line')
for question_link in question_links:
    # print(link.text)
    link = question_link.find('a').attrs['href']
    print(link)