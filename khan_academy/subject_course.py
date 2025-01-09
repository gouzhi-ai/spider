#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/8 下午3:33
# @Author  : 苏玉恒
# @File    : subject_course.py
# @Software: PyCharm

import json

import requests

def get_subject_course():
    file_path = 'learnMenuTopicsQuery.json'
    data = json.load(open(file_path, 'r', encoding='utf-8'))
    data = data["data"]["learnMenuTopics"]

    print(data)

    subject_course = []

    for subject in data:
        one_subject = {
            "subjectId": subject["domainId"],
            "subjectSlug": subject["slug"],
            "subjectName": subject["translatedTitle"],
            "subjectChildren": []
        }
        for child in subject["children"]:
            one_course = {
                "courseId": child["courseId"],
                "courseSlug": child["slug"],
                "courseName": child["translatedTitle"],
            }
            one_subject["subjectChildren"].append(one_course)
        subject_course.append(one_subject)

    # print(subject_course[0]["subjectChildren"][12])
    return subject_course



print(get_subject_course())