# -*- codeing = utf-8 -*-
# @Time : 2021/7/15 20:45
# @Author : 小觐
# @File : testSqlite.py
# @Software : PyCharm

import sqlite3

# 1.连接数据库
# con = sqlite3.connect("test.db")  # 创建数据库文件
# print("已成功打开数据库")

# 2.创建数据表

con = sqlite3.connect("test.db")  # 创建数据库文件

print("成功打开数据库")
c = con.cursor()  # 获取游标
sql = '''
    create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(255),
        salary real);
'''
c.execute(sql)  # 执行SQL语句
con.commit()  # 提交数据库操作
con.close()  # 关闭连接

print("成功建表")

# 3.插入数据

# 4.查询数据
