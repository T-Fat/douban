# -*- codeing = utf-8 -*-
# @Time : 2021/7/14 22:12
# @Author : 小觐
# @File : testXwlt.py
# @Software : PyCharm


import xlwt

# workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
# worksheet = workbook.add_sheet('sheet1')  # 创建工作表
# worksheet.write(0, 0, 'hello')  # 行，列，写入内容
# workbook.save('student.xls')  # 保存数据表

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('99biao')
s = ''
for i in range(0, 9):
    for j in range(0, i + 1):
        s=str('%d*%d=%d' % (j + 1, i + 1, (i + 1) * (j + 1)))
        worksheet.write(i,j,s)
workbook.save('student.xls')
