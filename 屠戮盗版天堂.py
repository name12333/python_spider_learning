import requests
import re
from urllib.parse import urljoin
import urllib3

# 禁用InsecureRequestWarning警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 定义常量
BASE_URL = r'https://www.dytt8899.com/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
}

try:
    # 发送HTTP请求并处理异常，暂时跳过SSL验证（仅用于测试目的）
    response = requests.get(BASE_URL, verify=False, headers=HEADERS, timeout=10)
    response.raise_for_status()  # 检查HTTP错误
    # 自动检测编码
    response.encoding = response.apparent_encoding or 'utf-8'

    # 编译正则表达式对象，用于提取2025必看热片的ul内容
    obj1 = re.compile(r'2025必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
    # 编译正则表达式对象，用于提取href链接
    obj2 = re.compile(r'a href="(?P<href>.*?)"', re.S)

    
    result1 = obj1.finditer(response.text)
    child_href_list = []
    for it in result1:
        ul = it.group('ul')
        # 提取子页面链接
        result2 = obj2.finditer(ul)
        for itt in result2:
            child_href = BASE_URL+itt.group('href').strip('/')
            child_href_list.append(child_href)
    for href in child_href_list:
        child_response = requests.get(href, verify=False, timeout=10)
        child_response.encoding = response.apparent_encoding or 'utf-8'
        print(child_response.text)

except requests.RequestException as e:
    print(f"网络请求发生错误: {e}")
except re.error as e:
    print(f"正则表达式匹配错误: {e}")
except Exception as e:
    print(f"程序执行过程中发生未预期的错误: {e}")