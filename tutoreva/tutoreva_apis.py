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
from cookies import cookies
from questionai.utils import get_13_timestamp_ms, get_time_str

subject = {
    "math": [
        "Calculus",
        "Probability and Statistics",
        "Linear Algebra"
    ],
    "physics": [
        "General Physics"
    ],
    "chemistry": [
        "Chemical Principle",
        "General Chemistry"
    ],
    "biology": [
        "Molecular Biology of the Cell",
        "General Biology"
    ],
    "history": [
        "History"
    ],
    "english": [
        "English"
    ],
    "law": [
        "Business Law"
    ]
}



class Tutoreva_AI_Apis:
    def __init__(self):
        self.base_url = "https://www.tutoreva.com/study-resources/"
        self.proxy_ip = get_proxy_ip()
        self.proxies = get_proxy(self.proxy_ip)
        self.setup_logging()

        self.category_name = ""
        self.subject_name = ""

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
    def get_index(self, page: str, category_name: str, subject_name: str, token: str, create_source: str = "seo",
                  pagesize: str = "10", proxies: dict = None):

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "app-version": "2.6",
            "authorization": f"Token {token}",
            "cache-control": "no-cache",
            # "device-id": "4f58e852-4850-4ec2-824d-645dac2c9a8c",
            "device-type": "2",
            "origin": "https://www.tutoreva.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.tutoreva.com/",
            "request-id": f"1399763-{get_time_str()}-61173db4f39a4512884ba5742b1f54ab",
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
            "page": f"{page}",
            "pagesize": f"{pagesize}",
            "create_source": f"{create_source}",
            "category_name": f"{category_name}",
            "subject_name": f"{subject_name}",
            "$t": f"{get_13_timestamp_ms()}"
        }

        self.logger.info(f'Getting index for {str(params)}')
        print(f"index  {str(params)} ")
        for i in range(5):
            try:
                requests.session().keep_alive = False
                response = requests.get(url=url, headers=headers, params=params, proxies=proxies, timeout=10)
                if response.status_code == 200:
                    self.logger.info(f'Getting index for {str(params)} success')
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
    def get_details(self, recognized_type_encoded: str, question_id_encoded: str, token: str, proxies: dict = None,
                    create_source: str = "seo"):

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "app-version": "2.6",
            "authorization": f"Token {token}",
            "cache-control": "no-cache",
            # "device-id": "4f58e852-4850-4ec2-824d-645dac2c9a8c",
            "device-type": "2",
            "origin": "https://www.tutoreva.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.tutoreva.com/",
            "request-id": f"1399763-{get_time_str()}-988c26dab367401e8202d642876752af",
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
            "recognized_type_encoded": f"{recognized_type_encoded}",
            "create_source": f"{create_source}",
            "question_id_encoded": f"{question_id_encoded}",
            "$t": f"{get_13_timestamp_ms()}"
        }

        self.logger.info(f'Getting details for {str(params)}  {self.base_url}')
        print(f"details {str(params)}")

        for i in range(1):
            try:
                requests.session().keep_alive = False
                response = requests.get(url, headers=headers, params=params, proxies=proxies, timeout=10)
                if response.status_code == 200:
                    self.logger.info(f'Getting details for {str(params)} success')
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

    # 列表页 url提取
    def get_index_data(self, index_text):
        print("get_index start")
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
    def get_details_data(self, details_text):
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

            one_page_simple_data = self.get_index_data(index_text)

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
                        self.logger.info(
                            f"Updated  one_simple_data['datePublished']:{one_simple_data['datePublished']}, initial_time:{initial_time}")
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
                    qa_data = self.get_details_data(details_text)
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

        for subject_id in subject_id_list:
            subject_name = subject[subject_id]
            try:
                all_qa = self.get_all_qa()
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

