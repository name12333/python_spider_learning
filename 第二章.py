from urllib.request import urlopen
import urllib.parse
# reponse = urlopen("http://www.python.org")
# print(reponse.read().decode("utf-8"))
# print(reponse.status)
# print(reponse.getheaders())

# data = bytes(urllib.parse.urlencode({"name":"germey"}),encoding="utf-8")
# response2 = urlopen("https://www.httpbin.org/post",data=data)
# print(response2.read().decode("utf-8"))


# import urllib.request

# request = urllib.request.Request("https://python.org")
# response3 = urllib.request.urlopen(request)
# print(response3.read().decode("utf-8"))

import requests
r = requests.get("https://www.baidu.com")
print(type(r))
