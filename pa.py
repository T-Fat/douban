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
    datalist = getData(baseurl)
    # savepath = "豆瓣电影Top250.xls"
    dbpath = "movie.db"
    # 3.保存数据
    # saveData(datalist, savepath)
    saveData2DB(datalist, dbpath)

    # askURL("https://movie.douban.com/top250?start=")


# 生成正则表达式对象，表示规则（字符串的模式）

# 影片链接
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包换在字符中
# 影片标题
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudg = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数25次 （左闭右开，但是正好250条）
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 2.逐一解析网页
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            data = []  # 保存一部电影的全部信息
            item = str(item)

            # 影片的详情页连接
            link = re.findall(findLink, item)[0]  # re库通过正则表达式来查找指定的字符串
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)  # 片名可能有一个中文名，没有外文名
            if len(titles) == 2:
                ctitle = titles[0]  # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉无关的/符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append("   ")  # 外国名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgNum = re.findall(findJudg, item)[0]
            data.append(judgNum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append("   ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+?)?/>(\s+)?', " ", bd)
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())  # 去掉前后空格

            datalist.append(data)
    # print(datalist)  # 验证采集信息
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    # 模拟浏览器头部信息，向豆瓣服务器发送消息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("UTF-8")
        # print(html)
    except Exception as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，本质上是高速浏览器，我们可以接收什么水平的

def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影TOP250', cell_overwrite_ok=True)
    col = ('电影详情链接', '图片链接', '影片中文名', '影片外文名', '评分', '评价数', '概况', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


def saveData2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
                insert into movie250 (
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values (%s)''' % ",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text, 
        pic_link text,
        cname text,
        ename text,
        score numeric,
        rated numeric,
        instroduction text,
        info text        
        )    
    '''  # 创建数据库
    conn = sqlite3.connect(dbpath)
    curses = conn.cursor()
    curses.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    # init_db("movietest.db")
    print('over!!!')
