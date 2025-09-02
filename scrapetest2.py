from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
with open("page3.html", mode="w", encoding="utf-8") as f:
    for child in bsObj.find("table", {"id": "giftList"}).children:
        print(child)
        f.write(str(child) + "\n")
print("网页内容已保存到 baidu.html 文件中")