#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : 苏玉恒
# @time    : 2024/11/25 下午3:49
# @function: the script is used to do something.
# @version : V1

import json
import logging

import requests
from bs4 import BeautifulSoup

from proxy import get_proxy, get_proxy_ip
from utils import is_later_than_yesterday_10am, get_datetime,is_network_available

subject = {
    '2': 'math',
    '3': 'history',
    '4': 'biology',
    '5': 'english',
    '6': 'physics',

    '7': 'chemistry',
    '8': 'geography',
    '9': 'law',
    '10': 'socialstudies',
    '11': 'technology',

    '34': 'business',
    '35': 'health',
    '41': 'medicine',
    '51': 'literature',

    'math': '2',
    'history': '3',
    'biology': '4',
    'english': '5',
    'physics': '6',
    'chemistry': '7',
    'geography': '8',
    'law': '9',
    'socialstudies': '10',
    'technology': '11',
    'business': '34',
    'health': '35',
    'medicine': '41',
    'literature': '51'
}


class Question_AI_Apis:
    def __init__(self):
        self.base_url = "https://www.questionai.com"
        self.proxy_ip = get_proxy_ip()
        self.proxies = get_proxy(self.proxy_ip)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('crawler.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    # 列表页
    def get_index(self, subjectId: str, page: str, proxies: dict = None, cookies_str: str = None):
        self.logger.info(f'Getting index for {subject[subjectId]} {page}')
        print(f"index {subject[subjectId]}  {page} ")
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "cookie": "QUESTION_AI_PCUID=4b7j8pjsgnky2bx13ikm247sc41b11_1732504216; "
                      "QUESTION_AI_UUID=137d57b0-eb38-4b8b-93c9-2b9945415ca7;"
                      " webcuid=31d62202f1b18bb6863b2950be98d233;"
                      " _ga=GA1.1.665193756.1732506073;"
                      " questionConfigPC=; _clck=100kn9t%7C2%7Cfr6%7C0%7C1790; "
                      "_clsk=1pewkzx%7C1732519712016%7C1%7C1%7Ci.clarity.ms%2Fcollect; _ga_WTWVD7G0P1=GS1.1.1732515476.3.1.1732523463.0.0.0",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": f"https://www.questionai.com/subject/{subject[subjectId]}/{page}",
            "sec-ch-ua": "\\Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        }
        url = "https://www.questionai.com/qai/chatweb/questionList"
        params = {
            "clientType": "1",
            "vc": "251",
            # "cuid": "4b7j8pjsgnky2bx13ikm247sc41b11_1732504216",
            "vcname": "1.0.0",
            "reqFrom": "browser",
            # "release": "2024.1125.110951",
            "lang": "en",
            "t": "1732523469268",
            "appId": "aihomework",
            "subjectId": f"{subjectId}",
            "pageNum": f"{page}",
            "pageSize": "10"
        }

        for i in range(1):
            try:
                response = requests.get(url, headers=headers, params=params, proxies=proxies)
                if response.status_code == 200:
                    self.logger.info(f'Getting index for {subject[subjectId]} {page} success')
                    # print(f"index {subject[subjectId]}  {page}  成功 ")
                    return response.text
                # else:
                #     self.proxy_ip = get_proxy_ip()
                #     self.proxies = get_proxy(self.proxy_ip)
            except Exception as e:
                self.logger.error(f"Crawling stopped due to error: {e}")
                self.proxy_ip = get_proxy_ip()
                self.proxies = get_proxy(self.proxy_ip)
                # print(f"Crawling stopped due to error: {e}")
        return "0"

    # 详情页
    def get_details(self, subjectId: str, page: str, url: str, proxies: dict = None, cookies_str: str = None):
        self.logger.info(f'Getting details for {subject[subjectId]}  {page}  {url}')
        print(f"details {subject[subjectId]}  {page} {url}")

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "referer": f"https://www.questionai.com/subject/{subject[subjectId]}/{page}",
            "sec-ch-ua": "\\Not)A;Brand;v=\\99, \\Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\\Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }
        cookies = {
            "QUESTION_AI_PCUID": "42u0uq459wsfyeu7rhndy53lwv97d2_1732600371",
            "QUESTION_AI_UUID": "4c1b5276-c523-48f7-875b-ba52ff34995e",
            "questionConfigPC": "",
            "webcuid": "21219abe634e3f2f283128ffd797c67b",
            "_ga": "GA1.1.270572433.1732600376",
            "_ga_WTWVD7G0P1": "GS1.1.1732604412.2.1.1732606465.0.0.0"
        }
        # url = "https://www.questionai.com/questions-tUTMuWhieW00/grade-point-averages-gpa-12-randomly-selected-college"

        for i in range(1):
            try:
                response = requests.get(url, headers=headers, cookies=cookies, proxies=proxies)
                if response.status_code == 200:
                    self.logger.info(f'Getting details for {subject[subjectId]} {page}  {url}success')
                    # print(f"details {subject[subjectId]}  {page}  成功  {url}")
                    return response.text
                else:
                    return "0"
                # else:
                #     self.proxy_ip = get_proxy_ip()
                #     self.proxies = get_proxy(self.proxy_ip)
            except Exception as e:
                self.logger.error(f"Crawling stopped due to error: {e}")
                self.proxy_ip = get_proxy_ip()
                self.proxies = get_proxy(self.proxy_ip)
                # print(f"Crawling stopped due to error: {e}")
        return "0"

    # 下载图片
    def get_img(self, url: str, proxies: dict = None):
        # print("-----------正在下载图片 ")
        self.logger.info(f'Getting image for {url}')
        # 这是一个图片的url

        response = requests.get(url, proxies=proxies)
        # 获取的文本实际上是图片的二进制文本
        img = response.content
        # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
        # 保存路径
        path = '20241128.jpg'

        return img

    # 列表页 url提取
    def get_urls(self, index_text):
        print("get_urls start")
        re_text = str(index_text)
        re_text = json.loads(re_text)
        re_text = re_text.get("data")
        index_list = re_text.get("list")
        one_page_urls = []
        for i in index_list:
            url = i.get("canonical")
            one_page_urls.append(url)

        print("get_urls success!")
        return one_page_urls

    # 详情页 问题、图片、答案、解释
    def get_one_data(self, details_text):
        print("get_one_data start")
        html = details_text
        soup = BeautifulSoup(html, "html.parser")
        qa_data = {}

        scripts = soup.find_all('script', {'type': 'application/ld+json'})
        for script in scripts:
            try:
                data = json.loads(script.string)
                if data.get('@type') == 'QAPage' and 'mainEntity' in data:
                    main_entity = data['mainEntity']
                    qa_data = {
                        'question': {
                            'text': main_entity.get('text', ''),
                            'image': main_entity.get('image', ''),
                            'image_byte': 1,
                            'author': main_entity.get('author', {}).get('name', ''),
                            'datePublished': main_entity.get('datePublished', ''),
                            'dateModified': main_entity.get('dateModified', '')
                        },
                        'answer': {
                            'text': main_entity.get('acceptedAnswer', {}).get('text', ''),
                            'author': main_entity.get('acceptedAnswer', {}).get('author', {}).get('name', ''),
                            'datePublished': main_entity.get('acceptedAnswer', {}).get('datePublished', ''),
                            'upvoteCount': main_entity.get('acceptedAnswer', {}).get('upvoteCount', 0)
                        },
                        'metadata': {
                            'answerCount': main_entity.get('answerCount', 0),
                            'upvoteCount': main_entity.get('upvoteCount', 0),
                            'url': main_entity.get('author', {}).get('url', '')
                        }
                    }
                    if "Explanation" in str(main_entity):  # QAPage 里面已经有了
                        pass
                    elif "Explanation" not in str(html):  # QAPage  里面没有  这个题目没题解
                        pass
                    else:  # QAPage  里面没有,  要在div里面找，，，，这是最特殊情况。
                        the_list = soup.find('div', {'class': 'answerScroll'})
                        if the_list:
                            explain = the_list.get_text(strip=True, separator='\n')
                            # Explanation
                            qa_data['answer']['text'] = qa_data['answer']['text'] + " Explanation " + explain
                        else:
                            print("No element found with class 'answerScroll'.")

                    # json_data_list.append(qa_data)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
                continue

        print(f"get_one_data success! {qa_data['metadata']['url']}")
        self.logger.info(f"get_one_data success!   QA answer datePublished {qa_data['answer']['datePublished']}")
        return qa_data

    # def insert_to_sql(data):
    #     conn = pymysql.connect(host="localhost", database="MYSQL", user='root',
    #                            password='123syh123', charset='utf8mb4')
    #
    #     cursor = conn.cursor()
    #     # 达人个人信息表
    #     insert_sql = ("INSERT INTO questionai VALUES (%s,%s, %s, %s)")
    #
    #     try:
    #         cursor.execute("USE lelekt;")
    #         cursor.execute(insert_sql, data)
    #         conn.commit()
    #         print("数据插入成功！")
    #     except pymysql.Error as e:
    #         print(f"数据插入失败：{e}")
    #     finally:
    #         cursor.close()
    #         conn.close()

    # def data_to_csv(data):
    #     with open('1.csv', 'a', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerows(data)
    #
    #     print("Data has been written to 1.csv")
    # def download_img(url_info):
    #     print("-----------正在下载图片 ")
    #     # 这是一个图片的url
    #     try:
    #
    #         response = requests.get(url)
    #         # 获取的文本实际上是图片的二进制文本
    #         img = response.content
    #         # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    #         # 保存路径
    #         path = '20241128.jpg'
    #         print(img)
    #         with open(path, 'wb') as f:
    #             f.write(img)
    #     except Exception as ex:
    #         print("--------出错继续----{}".format(ex))
    #         pass

    def get_all_qa(self, subjectId: str, start_page: int, end_page: int):
        print(f"Starting crawler from page {start_page} to {end_page}")

        all_qa = []

        for page in range(start_page, end_page + 1):
            subject_name = subject[subjectId]

            index_text = self.get_index(subjectId=subjectId, page=str(page), proxies=self.proxies)

            if index_text == "0":
                continue
            if not is_network_available():
                self.logger.error(f"Network is not available. subject_name={subject_name}, page={page}")
                continue

            all_urls = (self.get_urls(index_text))

            for url in all_urls:
                details_text = self.get_details(subjectId=str(subjectId), page=str(page), url=str(url),
                                                proxies=self.proxies)
                # print("details success {url} ")
                if details_text == "0":
                    continue
                try:
                    qa_data = self.get_one_data(details_text)
                except Exception as e:
                    print(f"Error parsing JSON: {e}")
                    continue

                if is_later_than_yesterday_10am(qa_data["answer"]["datePublished"]):
                    # todo
                    all_urls = []
                    end_page = page
                    # pass

                # img=""
                # try:
                #     img = self.get_img(url=str(url),proxies=self.proxies)
                # except Exception as e:
                #     print(f"get details: crawling stopped due to error: {e}")
                #     self.proxy_ip = get_proxy_ip()
                #     self.proxies = get_proxy(self.proxy_ip)
                #     img = self.get_img(url=str(url),proxies=self.proxies)
                #
                # qa_data["question"]["image_byte"] = img

                all_qa.append(qa_data)

        return all_qa

    # 采集所有科目 1-100页。
    def get_all_subject(self):
        subject_id_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '34', '35', '41', '51']
        # subject_id_list = ['2']
        for subject_id in subject_id_list:
            subject_name = subject[subject_id]
            all_qa = self.get_all_qa(subjectId=subject_id, start_page=1, end_page=100)
            save_list_to_json(all_qa, f"{subject_name}.json")


# def sql(all_data):
#
#
#     # 数据库连接字符串
#     conninfo = "host=172.16.223.100 port=35432 dbname=postgres user=postgres password=postgres"
#
#     try:
#         with psycopg.connect(conninfo) as conn:
#             conn.autocommit = True
#
#             with conn.cursor() as cur:
#                 # 创建简单的表结构
#                 cur.execute("""
#                     CREATE TABLE IF NOT EXISTS questionai (
#                         id SERIAL PRIMARY KEY,
#                         qa_data JSONB
#                     )
#                 """)
#
#                 # 假设你的数据列表名为qa_data_list
#                 for item in all_data:
#                     cur.execute(
#                         "INSERT INTO questionai (qa_data) VALUES (%s)",
#                         [psycopg.types.json.dumps(item)]
#                     )
#
#         print("数据已成功导入到PostgreSQL数据库中的question_ai表")
#
#     except Exception as e:
#         print(f"发生错误: {str(e)}")

def save_list_to_json(data_list, output_file):
    try:
        output_file = str(get_datetime()) + "_" + str(output_file)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)
        print(f"数据已成功保存到 {output_file}")
    except Exception as e:
        print(f"保存文件时发生错误: {str(e)}")


def scheduler_task_pre():
    question_ai_apis = Question_AI_Apis()
    question_ai_apis.get_all_subject()


if __name__ == '__main__':
    scheduler_task_pre()
