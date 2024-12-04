from datetime import datetime, timedelta, timezone
import requests
from requests.exceptions import RequestException
import time
import random


CHECK_URL = 'http://www.baidu.com'
def is_network_available():
    """检查网络是否可用"""
    try:
        # 发送一个简单的 GET 请求来检查网络
        response = requests.get(CHECK_URL, timeout=5)
        response.raise_for_status()
        return True
    except RequestException as e:
        print(f"Network check failed: {e}")
        return False

# 判断时间是否在昨天上午10点之后
def is_later_than_yesterday_10am(time_str):
    # 解析给定的时间字符串（假设输入格式为 ISO 8601）
    given_time = datetime.fromisoformat(time_str)

    # 获取今天的日期
    today = datetime.now(timezone.utc).date()

    # 计算昨天的日期
    yesterday = today - timedelta(days=1)

    # 创建昨天上午10点的时间，并设置为UTC时区
    ten_am_yesterday = datetime.combine(yesterday, datetime.min.time()) + timedelta(hours=10)
    ten_am_yesterday = ten_am_yesterday.replace(tzinfo=timezone.utc)

    # print(ten_am_yesterday)

    # 比较给定时间和昨天上午10点
    return given_time > ten_am_yesterday


# 输出当前的年月日
def get_datetime():
    # 获取当前日期和时间
    now = datetime.now()

    # 输出当前的年月日
    print(now.strftime("%Y-%m-%d"))


# 测试函数
def test():
    get_datetime()


if __name__ == '__main__':
    test()
