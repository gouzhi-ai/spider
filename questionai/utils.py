from datetime import datetime, timedelta, timezone
import requests
from requests.exceptions import RequestException
import time
import random
import json
import os

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



# 获取当前日期时间
# 格式化为 YYYYMMDDHHMMSS 形式的字符串
def get_time_str():
    formatted_time = datetime.now().strftime('%Y%m%d%H%M%S')
    return formatted_time


# 获取13位时间戳
# 获取当前时间，并调用 timestamp() 方法获取时间戳（秒），然后乘以1000得到毫秒
def get_13_timestamp_ms():
    timestamp_ms = int(datetime.now().timestamp() * 1000)
    return timestamp_ms


def compare_time(time_a: str, time_b: str) -> bool:
    try:
        # 将ISO 8601格式的字符串转换为datetime对象
        dt_a = datetime.fromisoformat(time_a.replace('Z', '+00:00'))
        dt_b = datetime.fromisoformat(time_b.replace('Z', '+00:00'))

        # 比较两个时间，如果a早于b返回True
        return dt_a < dt_b
    except ValueError as e:
        print(f"错误：输入的时间格式不正确 - {e} ,time_a:{time_a},time_a: {time_b}")
        return False


# 判断时间是否在昨天上午10点之后
def is_later_than_yesterday_10am(time_str):
    # 解析给定的时间字符串（假设输入格式为 ISO 8601）
    given_time = datetime.fromisoformat(time_str)

    # 获取今天的日期
    today = datetime.now(timezone.utc).date()

    # 计算昨天的日期
    yesterday = today - timedelta(days=1)
    # print(yesterday)

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
    return now.strftime("%Y-%m-%d")


def get_json_time(key: str) -> str:
    try:
        # 检查文件是否存在
        if not os.path.exists('update_time.json'):
            print("错误：update_time.json 文件不存在")
            return None

        # 读取JSON文件
        with open('update_time.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 获取指定键的值
        if key in data:
            return data[key]
        else:
            print(f"警告：在JSON中未找到键 '{key}'")
            return None

    except json.JSONDecodeError:
        print("错误：JSON文件格式不正确")
        return None
    except Exception as e:
        print(f"错误：读取文件时发生异常 - {str(e)}")
        return None


def update_json_time(key: str, new_value: str) -> bool:
    try:
        file_path = 'update_time.json'

        # 如果文件不存在，创建一个新的
        if not os.path.exists(file_path):
            initial_data = {}
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(initial_data, f, ensure_ascii=False, indent=4)
            print(f"创建了新的文件：{file_path}")

        # 读取现有的JSON数据
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 更新值
        data[key] = new_value

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"成功更新键 '{key}' 的值为 '{new_value}'")
        return True

    except json.JSONDecodeError:
        print("错误：JSON文件格式不正确")
        return False
    except Exception as e:
        print(f"错误：操作文件时发生异常 - {str(e)}")
        return False


# 使用示例
def test():
    # 假设update_time.json内容如下：
    # {
    #     "key1": "2024-03-14T10:00:00Z",
    #     "key2": "2024-03-14T11:00:00Z"
    # }

    result = get_13_timestamp_ms()
    print(result)  # 输出对应的值或None


if __name__ == '__main__':
    test()
    # print(1)