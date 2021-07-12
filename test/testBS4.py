# -*- coding: UTF-8 -*-
# @Time : 2021/7/12 9:18
# @Author : 李觐

from bs4 import BeautifulSoup

fiLe = open("./baidu.html", "rb")
html = fiLe.read()
bs = BeautifulSoup(html, "html.parser")
# 1.Tag  标签及其内容，拿到他所找到的第一个内容
print(bs.a)
print(type(bs.a))
# 2.NavigableString  标签里的内容（字符串）
print(bs.p.string)
print(type(bs.p.string))
# 拿到标签的属性
print(bs.a.attrs)
# 3.BeautifulSoup  表示整个文档
print(type(bs))
print(bs.name)
# print(bs)
# 4.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号
print(bs.a.string)
print(type(bs.a.string))
