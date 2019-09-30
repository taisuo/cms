from django.shortcuts import render
from datetime import date
from datetime import datetime
from django.http import HttpResponse
# Create your views here
import json
import pymysql
# Create your views here.
def acticleList(request):
    return render(request, "acticle/acticleList.html")
def acticleListHandle(request):
    return render(request, "acticle/acticleList.html")

def addActicle(request):
    return render(request, "acticle/addActicle.html")
def addActicleHandle(request):
    return render(request, "acticle/acticleList.html")
def list(request):

    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='user1',  ##数据库名
        charset='utf8'  ##连接编码
    )
    print("12")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # sql = "SELECT * FROM userlist"
    # cursor.execute(sql)
    # rr = cursor.fetchall()
    # print(cursor.rowcount)
    # now = datetime.now()
    # sql = "INSERT INTO userinfo(uid,title,content,usertime)values (%s,%s,%s,%s);"
    # data = [('1', '文章i', '文章内容i', '2019-08-12 12:12:12'),('1', '文章i', '文章内容i', '2019-08-12 12:12:12')]
    # cursor.executemany(sql, data)
    # conn.commit()
    # now = datetime.now()
    # sql = "INSERT INTO userinfo(uid,title,content,usertime)values (%s,%s,%s,%s);"
    # data = []
    # data1=()
    # for i in range(1,800):
    #     _data=i, '文章%d', '文章内容%d', '2019-08-12 12:12:12'
    #     data1=_data
    #     data.append(data1)
    # print(data)
    # cursor.executemany(sql, data)
    # conn.commit()
    # sql = "UPDATE userinfo set uid='%s' where id<'%s'"
    # data = ("1", 14)
    # cursor.execute(sql % data)
    # conn.commit()
    # sql = "DELETE FROM userinfo WHERE  id='%s'"
    # data = (1)
    # cursor.execute(sql % data)
    # conn.commit()
    # sql="SELECT * FROM userinfo ORDER BY uid ASC limit 1,20 "
    # sql = "SELECT * FROM userinfo ORDER BY uid ASC limit 1,20 "
    # cursor.execute(sql)
    # conn.commit()
    # aa = cursor.fetchall()
    # print(cursor.rowcount)
    # print(aa)
    sql = "SELECT * FROM userinfo"
    cursor.execute(sql)
    print(cursor.rowcount)
    return render(request, "acticle/list.html")
































