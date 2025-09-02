import re
# findall:在字符串中找到所有匹配正则表达式的内容，并以列表形式返回
lst = re.findall(r"\d+","我的电话号是：10086,我的邮箱是：10086@163.com")
print(lst)
# finditer:在字符串中找到所有匹配正则表达式的内容，并以迭代器返回,从迭代器中获取内容需要.goup()方法
iter =re.finditer(r"\d+","我的电话号是：10086,我的邮箱是：10086@163.com")
for i in iter:
    print(i.group())
# search:在字符串中搜索第一个匹配正则表达式的内容，并以match对象形式返回,从对象中获取内容需要.goup()方法
s =  re.search(r"\d+","我的电话号是：10086,我的邮箱是：10086@163.com")
print(s.group())
# # match:在字符串开头匹配正则表达式的内容，默认在你的正则表达式形式是"^\d+ "，并以match对象形式返回,从对象中获取内容需要.goup()方法
# m = re.match(r"\d+","我的电话号是：10086,我的邮箱是：10086@163.com")
# print(m.group())
# compile:将正则表达式编译成正则表达式对象，对象可以缓存正则表达式，下次使用可以提高效率
obj = re.compile(r"\d+")
print(obj.findall("我的电话号是：10086,我的邮箱是：10086@163.com"))
