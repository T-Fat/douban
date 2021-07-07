# -*- codeing = utf-8 -*-
# @Time : 2021/7/7 20:52
# @Author : 小觐
# @File : pa.py
# @Software : PyCharm


from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则
import urllib.request, urllib.error  # 指定URL，获取网页数据
import xlwt  # 进行Excel操作
import sqlite3  # 进行sqllite3数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalsit = getData(baseurl)
    # 3.保存数据
    savepath = ".\\豆瓣电影Top250.xls"


# 爬取网页
def getData(baseurl):
    datalist = []
    # 2.解析网页
    return datalist


def saveData(savepath):
    print("save")


if __name__ == '__main__':
    main()
