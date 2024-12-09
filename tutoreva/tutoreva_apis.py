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

from questionai.proxy import get_proxy, get_proxy_ip
from questionai.utils import compare_time, get_datetime, is_network_available, get_json_time, update_json_time


subject={

}

class Tutoreva_AI_Apis:
    def __init__(self):
        self.base_url = "https://www.tutoreva.com/study-resources/"
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
        self.logger.info(f'Getting index for {subject} {page}')
        print(f"index {subject}  {page} ")


        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "app-version": "2.6",
            "authorization": "Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTM5OTc2MywidXNlcl9tb2RlbF9uYW1lIjoiVXNlckFwcCIsImV4cGlyZV90aW1lIjoiMjAyNC0xMi0xMlQwOTo0NDo1NC4xNzc3NjUiLCJhY3QiOiJ0b2tlbiIsImRpZmYiOjI1OTIwMH0.qG1wq2sMMXmX79cc1_TgC17HzcrIqkoC1NAZG_76Qq0",
            "cache-control": "no-cache",
            "device-id": "4f58e852-4850-4ec2-824d-645dac2c9a8c",
            "device-type": "2",
            "origin": "https://www.tutoreva.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.tutoreva.com/",
            "request-id": "1399763-20241210170648-61173db4f39a4512884ba5742b1f54ab",
            "sec-ch-ua": "\\Not)A;Brand;v=\\99, \\Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\\Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }
        url = "https://luffy.tutoreva.com/photograph_searching/seo/questions/list/"
        params = {
            "page": "1",
            "pagesize": "10",
            "create_source": "seo",
            "category_name": "math",
            "subject_name": "Calculus",
            "$t": "1733821608949"
        }

        for i in range(1):
            try:
                requests.session().keep_alive = False
                response = requests.get(url, headers=headers, params=params, proxies=proxies, timeout=10)
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
        self.logger.info(f'Getting details for {subject}  {page}  {url}')
        print(f"details {subject}  {page} {url}")


        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "app-version": "2.6",
            "authorization": "Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTM5OTc2MywidXNlcl9tb2RlbF9uYW1lIjoiVXNlckFwcCIsImV4cGlyZV90aW1lIjoiMjAyNC0xMi0xMlQwOTo0NDo1NC4xNzc3NjUiLCJhY3QiOiJ0b2tlbiIsImRpZmYiOjI1OTIwMH0.qG1wq2sMMXmX79cc1_TgC17HzcrIqkoC1NAZG_76Qq0",
            "cache-control": "no-cache",
            "device-id": "4f58e852-4850-4ec2-824d-645dac2c9a8c",
            "device-type": "2",
            "origin": "https://www.tutoreva.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.tutoreva.com/",
            "request-id": "1399763-20241210171908-988c26dab367401e8202d642876752af",
            "sec-ch-ua": "\\Not)A;Brand;v=\\99, \\Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\\Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }
        url = "https://luffy.tutoreva.com/photograph_searching/seo/questions/detail/"
        params = {
            "recognized_type_encoded": "tq",
            "create_source": "seo",
            "question_id_encoded": "9af4",
            "$t": "1733822348787"
        }

        for i in range(1):
            try:
                requests.session().keep_alive = False
                response = requests.get(url, headers=headers, params=params, proxies=proxies, timeout=10)
                if response.status_code == 200:
                    self.logger.info(f'Getting details for {subject} {page}  {url}  success')
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
    # def get_img(self, url: str, proxies: dict = None):
    #     # print("-----------正在下载图片 ")
    #     self.logger.info(f'Getting image for {url}')
    #     # 这是一个图片的url
    #     requests.session().keep_alive = False
    #
    #     response = requests.get(url, proxies=proxies, timeout=10)
    #     # 获取的文本实际上是图片的二进制文本
    #     img = response.content
    #     # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    #     # 保存路径
    #     path = '20241128.jpg'
    #
    #     return img


    # 列表页 url提取
    def get_simple_data(self, index_text):
        print("get_urls start")
        re_text = str(index_text)
        re_text = json.loads(re_text)
        re_text = re_text.get("data")
        index_list = re_text.get("list")
        one_page_simple_data = []

        for i in index_list:
            one_simple_data = {
                "url": i.get("canonical"),
                "contentLatex": i.get("contentLatex"),
                "imageURL": i.get("imageURL"),
                "datePublished": i.get("datePublished")
            }
            one_page_simple_data.append(one_simple_data)

        print("get_urls success! ")
        return one_page_simple_data

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
                            # 'image_byte': 1,
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
        self.logger.info(f"{subject[subjectId]} Starting crawler from page {start_page} to {end_page}")
        subject_name = subject[subjectId]
        all_qa = []
        # 记录json文件里记录的的原始时间
        initial_time = get_json_time(subject_name)
        # 状态值：标记是否开始采集详情页
        status = 0
        for page in range(start_page, end_page + 1):
            index_text = self.get_index(subjectId=subjectId, page=str(page), proxies=self.proxies)

            if index_text == "0":
                continue
            if not is_network_available():
                self.logger.error(f"Network is not available. subject_name={subject_name}, page={page}")
                continue

            one_page_simple_data = self.get_simple_data(index_text)

            for one_simple_data in one_page_simple_data:

                try:
                    if compare_time(one_simple_data['datePublished'], initial_time):
                        # 没更新
                        self.logger.info(
                            f"Not updated"
                            f"datePublished:{one_simple_data['datePublished']} initial_time：{initial_time}  "
                            f"result： {compare_time(one_simple_data['datePublished'], initial_time)}")
                        return all_qa
                    elif status == 0:
                        status = 1
                        # 更新了
                        self.logger.info("Updated")
                        update_json_time(subject_name, one_simple_data['datePublished'])
                except Exception as e:
                    print(one_simple_data)
                    print(f"Exception:{e}  {initial_time}")
                    continue
                # continue

                details_text = self.get_details(subjectId=str(subjectId), page=str(page),
                                                url=str(one_simple_data['url']), proxies=self.proxies)

                if details_text == "0":
                    continue
                try:
                    qa_data = self.get_one_data(details_text)
                    qa_data['question']['text'] = one_simple_data['contentLatex']
                    qa_data['question']['image'] = one_simple_data['imageURL']
                except Exception as e:
                    print(f"Error parsing JSON: {e}")
                    continue

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
        # subject_id_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '34', '35', '41', '51']
        subject_id_list = ['2', '3', '4', '5', '6',
                           '7', '8', '51']
        # subject_id_list = ['2']  # test
        for subject_id in subject_id_list:
            subject_name = subject[subject_id]
            if subject_id=='7':continue
            if subject_id=='8':continue
            if subject_id=='51':continue
            try:
                all_qa = self.get_all_qa(subjectId=subject_id, start_page=1, end_page=100)
                save_list_to_json(all_qa, f"{subject_name}.json")
            except Exception as e:
                print(f"Error parsing JSON: {e}")
                self.proxy_ip = get_proxy_ip()
                self.proxies = get_proxy(self.proxy_ip)

def save_list_to_json(data_list, output_file):
    try:
        output_file = str(get_datetime()) + "_" + str(output_file)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)
        print(f"数据已成功保存到 {output_file}")
    except Exception as e:
        print(f"保存文件时发生错误: {str(e)}")


def scheduler_task_pre():
    tutoreva_ai_apis = Tutoreva_AI_Apis()
    tutoreva_ai_apis.get_all_subject()


if __name__ == '__main__':
    # scheduler_task_pre()
    print("start!")
