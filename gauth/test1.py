#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/18 下午4:08
# @Author  : 苏玉恒
# @File    : test1.py
# @Software: PyCharm

# 导入
from DrissionPage import Chromium

# 连接浏览器
browser = Chromium()
# 获取标签页对象
tab = browser.latest_tab
# 访问网页
tab.get('https://www.gauthmath.com/study-resources/math/popular/1')
