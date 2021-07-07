# -*- codeing = utf-8 -*-
# @Time : 2021/7/7 20:57
# @Author : 小觐
# @File : testUrllib.py
# @Software : PyCharm

import urllib.request
import urllib.parse

# 获取一个get请求
# response = urllib.request.urlopen('https://www.baidu.com')
# print(response)
# print(response.read().decode('utf-8'))

# 获取一个Post请求
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("https://httpbin.org/post", data=data)
# print(response)
# print(response.read().decode('utf-8'))

# 超时处理
# try:
#     response = urllib.request.urlopen("https://httpbin.org/get",timeout=2)
#     print(response.read().decode('utf-8'))
# except Exception as e:
#     print("timeout")

# response = urllib.request.urlopen("https://www.baidu.com", timeout=2)
# print(response.getheader("Date"))
# print(response.getheader("Set-Cookie"))
# print(response.read().decode('utf-8'))


url = "https://www.douban.com"
# url = "https://httpbin.org/post"
herders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
# data = bytes(urllib.parse.urlencode({"name": "a"}), encoding="utf-8")
req = urllib.request.Request(url=url, headers=herders)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
