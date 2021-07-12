# -*- coding: UTF-8 -*-
# @Time : 2021/7/12 9:56
# @Author : 李觐

import re

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# 文档的遍历
print(bs.head.contents[1])
# 更多内容搜索BeautifulSoup文档


# 文档的搜索
# 1
# 字符串过滤，会查找与字符串完全匹配的内容
t_list = bs.find_all("p")

# 正则表达式搜索：使用search()方法来匹配内容
t_list2 = bs.find_all(re.compile("p"))


# 方法:传入一个函数(方法),根据函数的要求搜索
def name_is_exists(tag):
    return tag.has_attr("name")


t_list3 = bs.find_all(name_is_exists)

# 2.kwargs   参数
t_list4 = bs.find_all(id="head")
t_list5 = bs.find_all(class_=True)

# 3.text参数
t_list6 = bs.find_all(text=["hao123", "新闻"])

# 4.limit 参数
t_list7 = bs.find_all("a", limit=3)

# css选择器
t_list8 = bs.select("title")  # 通过标签查找
t_list9 = bs.select(".mnav")  # 通过类名查找
t_list10 = bs.select("#u1")  # id查找
t_list11 = bs.select("a[class='s-top-login-btn c-btn "
                     "c-btn-primary c-btn-mini lb']")  # 通过属性查找
t_list12 = bs.select("body>div>div>div>div>div>div>div")  # 通过子标签查找
# 兄弟标签
for i in t_list12:
    print(i)
