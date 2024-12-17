#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : 苏玉恒
# @time    : 2024/11/25 下午3:49
# @function: the script is used to do something.
# @version : V1

import json
import logging
import time
import requests

from questionai.proxy import get_proxy, get_proxy_ip
from questionai.utils import get_datetime, is_network_available, sleep_time
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
        self.token = cookies[0]["token"]
        self.page = ''

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('tutoreva_crawler.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    # 列表页
    def get_index(self, page: str, create_source: str = "seo",
                  pagesize: str = "10", proxies: dict = None):

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "app-version": "2.6",
            "authorization": f"Token {self.token}",
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
            "category_name": f"{self.category_name}",
            "subject_name": f"{self.subject_name}",
            "$t": f"{get_13_timestamp_ms()}"
        }

        self.logger.info(
            f'Getting index for page={page},category_name={self.category_name},subject_name={self.subject_name}')
        for i in range(5):
            try:
                requests.session().keep_alive = False
                response = requests.get(url=url, headers=headers, params=params, proxies=proxies, timeout=10)
                if response.status_code == 200:
                    self.logger.info(
                        f'Getting index for page={page},category_name={self.category_name},subject_name={self.subject_name} success')
                    return response.text
            except Exception as e:
                self.logger.error(f"Crawling stopped due to error: {e}")
                self.logger.error(
                    f"Get error : page={page},category_name={self.category_name},subject_name={self.subject_name} ")
                self.proxy_ip = get_proxy_ip()
                self.proxies = get_proxy(self.proxy_ip)
        return "0"

    # 详情页
    def get_details(self, recognized_type_encoded: str, question_id_encoded: str, proxies: dict = None,
                    create_source: str = "seo"):

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "app-version": "2.6",
            "authorization": f"Token {self.token}",
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

        self.logger.info(
            f'Getting details for  page={self.page},category_name={self.category_name},subject_name={self.subject_name},recognized_type_encoded={recognized_type_encoded},question_id_encoded={question_id_encoded} ')

        for i in range(1):
            try:
                requests.session().keep_alive = False
                response = requests.get(url, headers=headers, params=params, proxies=proxies, timeout=10)
                if response.status_code == 200:
                    self.logger.info(
                        f'Getting details for  page={self.page},category_name={self.category_name},subject_name={self.subject_name},recognized_type_encoded={recognized_type_encoded},question_id_encoded={question_id_encoded}   success')
                    # print(response.text)
                    return response.text
                else:
                    return "0"
            except Exception as e:
                self.logger.error(f"Crawling stopped due to error: {e}")
                self.logger.error(
                    f"Get error : page={self.page},category_name={self.category_name},subject_name={self.subject_name},recognized_type_encoded={recognized_type_encoded},question_id_encoded={question_id_encoded} ")
                self.proxy_ip = get_proxy_ip()
                self.proxies = get_proxy(self.proxy_ip)
        return "0"

    # 列表页 url提取
    def get_index_data(self, index_text):
        self.logger.info(
            f"get_index_data start :page={self.page},category_name={self.category_name},subject_name={self.subject_name}")
        re_text = str(index_text)
        re_text = json.loads(re_text, strict=False)
        re_text = re_text.get("data")
        base_data = {
            "count": re_text.get("count"),
            "page": re_text.get("page"),
            "pages": re_text.get("pages"),
            "pagesize": re_text.get("pagesize"),
        }
        index_list = re_text.get("lists")
        one_page_index_data = []

        for i in index_list:
            one_simple_data = {
                "id": i.get("id"),
                "question_id": i.get("question_id"),
                "recognized_type": i.get("recognized_type"),
                "category_name": i.get("category_name"),
                "subject_name": i.get("subject_name"),
                "seo_html_url": i.get("seo_html_url"),
                "recognized_type_encoded": "",
                "question_id_encoded": ""
            }
            string_list = one_simple_data["seo_html_url"].split('-')[-2:]
            one_simple_data["recognized_type_encoded"] = string_list[0]
            one_simple_data["question_id_encoded"] = string_list[1]

            one_page_index_data.append(one_simple_data)

        self.logger.info(
            f"get_index_data success! page={self.page},category_name={self.category_name},subject_name={self.subject_name}")
        return [base_data, one_page_index_data]

    # 详情页 数据提取
    def get_details_data(self, details_text):
        self.logger.info("get_details_data start")
        qa_data = {}
        try:
            data = json.loads(details_text, strict=False)
            if data.get('code') == 200:
                data = data.get('data')
                result = data.get('result')
                recognized_type = result.get('recognized_type')
                main_entity = result.get(recognized_type)

                question = main_entity.get('stem', {})
                answer = main_entity.get('answer_subjective', {})
                explain = main_entity.get('steps', {})

                explain_list = []
                for i in explain:
                    text = i.get('text', {})
                    one_explain = {
                        'explain_id': i.get('id', ''),
                        'question_id': i.get('question_id', ''),
                        'name': i.get('name', ''),
                        'text': {
                            'text': text.get('text', ''),
                            'image_list': text.get('image_list', []),
                            'mix_list': text.get('mix_list', [])
                        }
                    }
                    explain_list.append(one_explain)
                qa_data = {
                    'question': {
                        'text': question.get('text', ''),
                        'image_list': question.get('image_list', []),
                        'mix_list': question.get('mix_list', [])
                    },
                    'answer': {
                        'text': answer.get('text', ''),
                        'image_list': answer.get('image_list', []),
                        'mix_list': answer.get('mix_list', [])
                    },
                    'original_image_url': result.get('original_image_url', ''),
                    'explain': explain_list,
                    'metadata': {
                        'seo_category_name': result.get('seo_category_name', ''),
                        'seo_subject_name': result.get('seo_subject_name', ''),
                        'subject': result.get('subject', ''),
                        'seo_html_url': result.get('seo_html_url', ''),
                        'url': f"https://www.tutoreva.com/study-resources/{result.get('subject', '')}-homework-help/{result.get('seo_html_url', '')}",
                        'id': main_entity.get('id', ''),
                    }
                }

        except Exception as e:
            self.logger.error(f"Error in get_details_data: {e}")

        self.logger.info(
            f"get_details_data success! {qa_data.get('metadata', '').get('url', '')},page={self.page},category_name={self.category_name},subject_name={self.subject_name}")
        return qa_data

    def get_all_qa(self, category_name: str, subject_name: str):
        self.logger.info(f"category_name={self.category_name},subject_name={self.subject_name} Starting crawler ")
        all_qa = []

        # 状态值：标记是否开始采集详情页
        status = 0
        for page in range(1, 10000 + 1):

            self.page = page
            if not is_network_available():
                self.logger.error(
                    f"Network is not available.  category_name= {category_name}, subject_name={subject_name}, page={page}")
                continue

            index_text = self.get_index(page=str(self.page))  # , proxies=self.proxies)

            if index_text == "0":
                continue

            one_index_data = self.get_index_data(index_text)
            pages = int(one_index_data[0]["pages"])
            self.logger.info(f"one_index_data[0]:{one_index_data[0]}")
            one_index_data = one_index_data[1]
            for one_details_data in one_index_data:
                # 判断是否 更新
                # 代码
                # todo
                recognized_type_encoded = one_details_data["recognized_type_encoded"]
                question_id_encoded = one_details_data["question_id_encoded"]
                details_text = self.get_details(recognized_type_encoded=recognized_type_encoded,
                                                question_id_encoded=question_id_encoded, )  # , proxies=self.proxies)

                if details_text == "0":
                    continue
                try:
                    qa_data = self.get_details_data(details_text)
                except Exception as e:
                    self.logger.error(
                        f"Error in get_all_qa: {e}  ,category_name= {category_name}, subject_name={subject_name}, "
                        f"page={page},recognized_type_encoded={recognized_type_encoded},question_id_encoded= {question_id_encoded},")
                    continue

                all_qa.append(qa_data)
                sleep_time()
            sleep_time()
            if int(page) == pages: break
        return all_qa

    # 采集所有科目
    def get_all_subject(self):
        for category_name in subject:
            self.category_name = category_name

            for subject_name in subject[category_name]:

                if category_name == "physics": continue
                if category_name == "math": continue
                if subject_name == "Chemical Principle": continue
                if subject_name == "Molecular Biology of the Cell": continue

                self.subject_name = subject_name
                self.logger.info(f"{category_name} {subject_name} Starting crawler ")
                # continue

                try:
                    all_qa = self.get_all_qa(category_name=self.category_name, subject_name=self.subject_name)
                    save_list_to_json(all_qa, f"{self.category_name}_{self.subject_name}.json")
                except Exception as e:
                    self.logger.error(f"Error in get_all_subject:: {e}")
                    self.proxy_ip = get_proxy_ip()
                    self.proxies = get_proxy(self.proxy_ip)
                # todo
                # break
            # break


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
    scheduler_task_pre()
