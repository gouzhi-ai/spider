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
        print("get_index_data start")
        re_text = str(index_text)
        re_text = json.loads(re_text,strict=False)
        re_text = re_text.get("data")
        base_data={
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
                "recognized_type_encoded":"",
                "question_id_encoded":""
            }
            string_list = one_simple_data["seo_html_url"].split('-')[-2:]
            one_simple_data["recognized_type_encoded"] = string_list[0]
            one_simple_data["question_id_encoded"] = string_list[1]

            one_page_index_data.append(one_simple_data)

        print("get_index_data success! ")
        return [base_data,one_page_index_data]

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

        for subject_id in subject:
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
    tutoreva_ai_apis = Tutoreva_AI_Apis()
    data="""{
    "code": 200,
    "msg": "success",
    "data": {
        "count": 96,
        "page": 1,
        "pages": 10,
        "pagesize": 10,
        "lists": [
            {
                "id": 1,
                "question_id": 39668,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "State the problem and objective Consider the function $f(t)=2.5 t^{2}+6 t$. The objective is to find the derivative of the function using the definition of derivative. Also, state the domain of the function and its derivative.",
                    "seo_html_url": "19-30-find-derivative-function-using-definition-derivative-state-domain-function-domain-deriv-tq-9af4",
                    "seo_description": "19–30 Find the derivative of the function using the definition of derivative. State the domain of the function and the domain of its derivative.21. f(t)=2.5 t2+6 t"
                },
                "original_image_url": "",
                "stem": "19–30 Find the derivative of the function using the definition of derivative. State the domain of the function and the domain of its \nderivative.\n21. $f(t)=2.5 t^{2}+6 t$",
                "status": "valid",
                "seo_html_url": "19-30-find-derivative-function-using-definition-derivative-state-domain-function-domain-deriv-tq-9af4"
            },
            {
                "id": 2,
                "question_id": 42434,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "Apply the definition of a derivative By definition:\n$f^\\prime(x)=\\lim _{h \\rightarrow 0} \\frac{f(x+h)-f(x)}{h}$\nIn this problem:\n$f^\\prime(x)=\\lim _{h \\rightarrow 0} \\frac{\\frac{2}{(x+h)^{2}}-\\frac{2}{x^{2}}}{h}$",
                    "seo_html_url": "10-11-find-f-prime-x-first-principles-directly-definition-derivative-10-f-x-frac-2-x-2-tq-a5c2",
                    "seo_description": "10-11 Find f'(x) from first principles, that is, directly from the definition of a derivative.10. f(x)=2/x2"
                },
                "original_image_url": "",
                "stem": "10-11 Find $f^{\\prime}(x)$ from first principles, that is, directly from the definition of a derivative.\n10. $f(x)=\\frac{2}{x^{2}}$",
                "status": "valid",
                "seo_html_url": "10-11-find-f-prime-x-first-principles-directly-definition-derivative-10-f-x-frac-2-x-2-tq-a5c2"
            },
            {
                "id": 3,
                "question_id": 46992,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "Work done formula The work done $W$ by a variable force $f(x)$ in moving a particle from $x=a$ to $x=b$ is given by the formula:\n$W=\\int_{a}^{b} f(x) d x$",
                    "seo_html_url": "4-variable-force-4-sqrt-x-newtons-moves-particle-along-straight-path-x-meters-origin-calculat-tq-b790",
                    "seo_description": "4. A variable force of 4 √(x) newtons moves a particle along a straight path when it is x meters from the origin. Calculate the work done in moving the particle from x=4 to x=16."
                },
                "original_image_url": "",
                "stem": "4. A variable force of $4 \\sqrt{x}$ newtons moves a particle along a straight path when it is $x$ meters from the origin. Calculate the work done in moving the particle from $x=4$ to $x=16$.",
                "status": "valid",
                "seo_html_url": "4-variable-force-4-sqrt-x-newtons-moves-particle-along-straight-path-x-meters-origin-calculat-tq-b790"
            },
            {
                "id": 4,
                "question_id": 67592,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "Identify the given curve and goal Given curve is $r=\\sin (\\frac\\theta 4)$.\nWe have to find the length of the curve correct to four decimal places using a calculator or computer.",
                    "seo_html_url": "59-62-use-calculator-computer-find-length-curve-correct-four-decimal-places-necessary-graph--tq-10808",
                    "seo_description": "59-62 Use a calculator or computer to find the length of the curve correct to four decimal places. If necessary, graph the curve to determine the parameter interval.62. r=sin(θ/ 4)"
                },
                "original_image_url": "",
                "stem": "59-62 Use a calculator or computer to find the length of the curve correct to four decimal places. If necessary, graph the curve to determine the parameter interval.\n62. $r=\\sin (\\theta / 4)$",
                "status": "valid",
                "seo_html_url": "59-62-use-calculator-computer-find-length-curve-correct-four-decimal-places-necessary-graph--tq-10808"
            },
            {
                "id": 5,
                "question_id": 65093,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "Define the condition for a statement to be always true or false The statement is always true or always false when the authenticity does not undergoes any sort of change for some particular condition or no counter example arises for the statement.",
                    "seo_html_url": "determine-whether-statement-true-false-true-explain-false-explain-give-example-disproves-stat-tq-fe45",
                    "seo_description": "Determine whether the statement is true or false. If it is true, explain why. If it is false, explain why or give an example that disproves the statement.7. Hydrostatic pressure on a dam depends only on the water level at the dam and not on the size of the reservoir created by the dam."
                },
                "original_image_url": "",
                "stem": "Determine whether the statement is true or false. If it is true, explain why. If it is false, explain why or give an example that disproves the statement.\n7. Hydrostatic pressure on a dam depends only on the water level at the dam and not on the size of the reservoir created by the dam.",
                "status": "valid",
                "seo_html_url": "determine-whether-statement-true-false-true-explain-false-explain-give-example-disproves-stat-tq-fe45"
            },
            {
                "id": 6,
                "question_id": 75189,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "Consider the iterated double integral Consider the iterated double integral,\n$\\int_{1}^{3} \\int_{1}^{5} \\frac{\\ln y}{x y} d y d x$.",
                    "seo_html_url": "15-26-calculate-iterated-integral-20-int-1-3-int-1-5-frac-ln-y-x-y-d-y-d-x-tq-125b5",
                    "seo_description": "15-26 Calculate the iterated integral.20. ∫13 ∫15 lny/x y d y d x"
                },
                "original_image_url": "",
                "stem": "15-26 Calculate the iterated integral.\n20. $\\int_{1}^{3} \\int_{1}^{5} \\frac{\\ln y}{x y} d y d x$",
                "status": "valid",
                "seo_html_url": "15-26-calculate-iterated-integral-20-int-1-3-int-1-5-frac-ln-y-x-y-d-y-d-x-tq-125b5"
            },
            {
                "id": 7,
                "question_id": 73499,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "Analyze the given equation It is given that $\\mathbf{r'}(t) = \\mathbf{c} \\times \\mathbf{r}(t)$.",
                    "seo_html_url": "35-particle-position-function-mathbf-r-t-mathbf-r-prime-t-mathbf-c-times-mathbf-r-t-mathbf-c-tq-11f1b",
                    "seo_description": "35. A particle has position function r(t). If r'(t)=c ×r(t), where c is a constant vector, describe the path of the particle."
                },
                "original_image_url": "",
                "stem": "35. A particle has position function $\\mathbf{r}(t)$. If $\\mathbf{r}^{\\prime}(t)=\\mathbf{c} \\times \\mathbf{r}(t)$, where $\\mathbf{c}$ is a constant vector, describe the path of the particle.",
                "status": "valid",
                "seo_html_url": "35-particle-position-function-mathbf-r-t-mathbf-r-prime-t-mathbf-c-times-mathbf-r-t-mathbf-c-tq-11f1b"
            },
            {
                "id": 8,
                "question_id": 129781,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "Define the function and constraints Define the function and constraints as follows:\n$f(x, y, z)=yz+xy; \\quad xy=1, \\quad y^{2}+z^{2}=1$",
                    "seo_html_url": "30-33-find-extreme-values-f-subject-constraints-33-f-x-y-z-y-z-x-y-x-y-1-y-2-z-2-1-tq-1faf5",
                    "seo_description": "30-33 Find the extreme values of f subject to both constraints.33. f(x, y, z)=y z+x y ; x y=1, y2+z2=1 "
                },
                "original_image_url": "",
                "stem": "30-33 Find the extreme values of $f$ subject to both constraints.\n33. $f(x, y, z)=y z+x y ; \\quad x y=1, \\quad y^{2}+z^{2}=1$ ",
                "status": "valid",
                "seo_html_url": "30-33-find-extreme-values-f-subject-constraints-33-f-x-y-z-y-z-x-y-x-y-1-y-2-z-2-1-tq-1faf5"
            },
            {
                "id": 9,
                "question_id": 61270,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "Analyze Given the integral $\\int_{1/4}^{\\sqrt{3}/4}\\sqrt{1-4x^2}\\mathrm{d}x$.\nThe expression $\\sqrt{1-4x^2}$ suggests the use of $\\begin{aligned}x=\\frac{1}{2}\\sin\\theta\\end{aligned}$. ",
                    "seo_html_url": "evaluate-integral-22-int-1-4-sqrt-3-4-sqrt-1-4-x-2-d-x-tq-ef56",
                    "seo_description": "Evaluate the integral.22. ∫1 / 4√(3) / 4 √(1-4 x2) d x"
                },
                "original_image_url": "",
                "stem": "Evaluate the integral.\n22. $\\int_{1 / 4}^{\\sqrt{3} / 4} \\sqrt{1-4 x^{2}} d x$",
                "status": "valid",
                "seo_html_url": "evaluate-integral-22-int-1-4-sqrt-3-4-sqrt-1-4-x-2-d-x-tq-ef56"
            },
            {
                "id": 10,
                "question_id": 74101,
                "recognized_type": "recognized_textbook_question",
                "category_name": "Math",
                "subject_name": "Calculus",
                "seo_info": {
                    "seo_answer": "Consider the function Consider the function $v=\\sin \\left(s^{2}-t^{2}\\right)$. Our objective is to find all the second derivatives.",
                    "seo_html_url": "47-52-find-second-partial-derivatives-51-v-sin-left-s-2-t-2-right-tq-12175",
                    "seo_description": "47-52 Find all the second partial derivatives.51. v=sin(s2-t2)"
                },
                "original_image_url": "",
                "stem": "47-52 Find all the second partial derivatives.\n51. $v=\\sin \\left(s^{2}-t^{2}\\right)$",
                "status": "valid",
                "seo_html_url": "47-52-find-second-partial-derivatives-51-v-sin-left-s-2-t-2-right-tq-12175"
            }
        ]
    }
}
    """
    result =tutoreva_ai_apis.get_index_data(index_text=data)
    print(result)