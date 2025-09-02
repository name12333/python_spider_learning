# ... existing code ...
"""
1. 拿到主页的源代码，然后提取子页面的链接地址，href
2. 通过href进入子页面，从子页面中找到img->src，拿到图片的地址
3. 通过图片地址，下载图片到本地
"""
import requests
from bs4 import BeautifulSoup
import time
import os

# 定义目标网站URL和请求头信息
url = r"https://www.umeituku.com/bizhitupian/weimeibizhi/"
# 添加请求头模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
}

try:
    # 发送GET请求获取网页内容
    with requests.get(url, headers=headers) as response:
        response.encoding = 'utf-8'  # 修复编码设置错误
        # print(response.text)
        # 使用BeautifulSoup解析网页内容
        page = BeautifulSoup(response.text, 'lxml')
        type_list_div = page.find("div", attrs={"class": "TypeList"})
        
        # 检查是否找到目标div元素
        if type_list_div is None:
            print("未找到TypeList div元素")
            exit()
            
        # 提取所有a标签
        alist = type_list_div.find_all("a")
        # print(alist)
        # 遍历每个a标签提取图片信息
        for a in alist:
            img = a.find("img")
            # print(img.get("src"));
            src = img.get("src")                
            try:
                # 请求图片资源
                with requests.get(src, headers=headers) as img_response:
                    img_response.raise_for_status()  # 检查请求是否成功
                    
                    # 拿到的是字节
                    # img_response= requests.get(src).content
                    # 从URL中提取图片名称并保存图片
                    img_name = src.split("/")[-1]
                    # 确保目标目录存在
                    os.makedirs("imag", exist_ok=True)
                    with open("imag/"+img_name, 'wb') as f:
                        f.write(img_response.content)
                    print(f"{img_name}下载完成")
            except requests.RequestException as e:
                print(f"下载图片 {src} 失败: {e}")
            except IOError as e:
                print(f"保存图片 {img_name} 失败: {e}")
                    
        # 控制请求频率，避免对服务器造成压力
        # time.sleep(1)
        
except requests.RequestException as e:
    print(f"获取网页 {url} 失败: {e}")
except Exception as e:
    print(f"发生未知错误: {e}")