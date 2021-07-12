# -*- coding: UTF-8 -*-
# @Time : 2021/7/12 9:56
# @Author : 李觐

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# 文档的遍历
print(bs.head.contents[1])
# 更多内容搜索BeautifulSoup文档


# 文档的搜索





