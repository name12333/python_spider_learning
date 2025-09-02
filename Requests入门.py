import requests
# 被拦截了
# query = input("请输入要搜索的内容:")
# url =f'https://www.sogou.com/web?query={query}'
# headers = {
#     "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36 Edg/139.0.0.0"
# }
# response = requests.get(url,headers=headers)
# print(response)

# url = r"https://fanyi.baidu.com/sug"
# s = input("请输入要翻译的内容:")
# data = {
#     "kw": s
# }
# response = requests.post(url,data=data)
# print(response.json())

url = r"https://movie.douban.com/j/chart/top_list"
params = {
    "type": "24",
    'interval_id': '100:90',
    'action':"",
    'start':0,
    'limit':20
}
header = {
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
}
response = requests.get(url,params=params,headers=header)
print(response.json())