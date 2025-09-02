import requests
from bs4 import BeautifulSoup

url = r"http://www.xinfadi.com.cn/index.html"
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',    
}
param = {
    'prodCatid':'1186'
}
response = requests.post(url,headers=header,params=param)
print(response.status_code)
print(response.text())
"""
BeautifulSoup 支持的几种解析器之一：
html.parser - Python 标准库中的 HTML 解析器，速度适中，容错性好
lxml - 第三方库，解析速度快，但需要额外安装
html5lib - 严格按照 HTML5 标准解析，最准确但速度较慢
"""
# page = BeautifulSoup(response.text,'lxml')
# #  获取表头
# header_row = page.find('table',attrs={'border':'0'})
# print(header_row)
# header_rlist = [th.get_tex(strip=True) for th in header_row.find_all('th')]
# # 提取表中内容
# table = page.find('tbody',attrs={'id':'tableBody'}).find_all('tr')
# data = []
# print(table)
# for t in table:
#     tds = t.find_all('td')
