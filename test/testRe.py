# -*- codeing = utf-8 -*-
# @Time : 2021/7/13 21:18
# @Author : 小觐
# @File : testRe.py
# @Software : PyCharm

# 正则表达式:字符串模式(判断字符串是否符合一定的标准)
import re

# 创建模式对象
pat = re.compile("AA")  # 正则表达式，用于验证其他字符串
m = pat.search("ACBAA")  # search字符串被校验的内容
print(m)
a = "AA"
b = "ABDKJDAAWEH"
n = re.search(a, b)
print(n)

print(re.findall("[A-Z]+", "ASADFasFDAfsStdfwqadwAsdwafd"))

# 把a换成A
print(re.sub("a", "A", r"fiosyuejakhfioruyeta\aoiurelkgjfhq"))
