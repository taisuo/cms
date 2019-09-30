from django.shortcuts import render,render_to_response
from datetime import date
from datetime import datetime
from django.http import HttpResponse
# Create your views here
import json
import pymysql
import random
# Create your views here.
def acticleList(request):
    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='blog',  ##数据库名
        charset='utf8'  ##连接编码
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "SELECT * FROM user"
    # cursor执行sql语句
    cursor.execute(sql)
    rr = cursor.fetchall()
    print(rr)
    sql1 = "SELECT * FROM article"
    # cursor执行sql语句
    cursor.execute(sql1)
    rr1 = cursor.fetchall()
    # return render(request, "acticle/acticleList.html")
    return render_to_response('acticle/acticleList.html', {'current_date': rr,'current_date1': rr1})
def acticleListHandle(request):
    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='blog',  ##数据库名
        charset='utf8'  ##连接编码
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql1= "SELECT * FROM article"
    # cursor执行sql语句
    cursor.execute(sql1)
    rr1 = cursor.fetchall()
    print(rr1)

    return render(request, "acticle/acticleList.html")

def addActicle(request):
    return render(request, "acticle/addActicle.html")
def addActicleHandle(request):
    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='blog',  ##数据库名
        charset='utf8'  ##连接编码
    )
    now = datetime.now()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    _title = request.POST.get("title")
    _content = request.POST.get("content")
    _userid = request.POST.get("userid")

    sql = "INSERT INTO article(title,uid,articletime)values (%s,%s,%s)"
    _data = (_title,_userid ,now)
    cursor.execute(sql,_data)
    conn.commit()
    sql1 = "select id from article where title=%s and uid= %s"
    data1 = (_title, _userid)
    cursor.execute(sql1, data1)
    rs = cursor.fetchone()
    print(rs["id"])
    sql2 = "INSERT INTO articlecontent(content,aid)values (%s,%s)"
    _data2 = (_content, rs["id"])
    cursor.execute(sql2, _data2)
    conn.commit()
    dic = {
        "code": 0,
        "msg": "发布成功",
    }
    dic.setdefault("uid", rs["id"])
    dic1 = json.dumps(dic)
    return HttpResponse(dic1)
def list(request):

    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='blog',  ##数据库名
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
    # sql = "UPDATE user SET username=%s WHERE username=%s"
    # newUsername = "张三" + str(random.randint(1, 10000))
    # print(newUsername)
    # data = (newUsername, "张三")
    # cursor.execute(sql, data)
    # conn.commit()
    # print("更新成功")
    # for i in range(1,800):
    #     _data=i, newUsername , '文章内容%d', 'new'
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
    # sql = "SELECT * FROM userinfo ORDER BY uid DESC limit 1,20 "
    # cursor.execute(sql)
    # conn.commit()
    # aa = cursor.fetchall()
    # print(cursor.rowcount)
    # print(aa)
    # sql = "SELECT * FROM userinfo"
    # cursor.execute(sql)
    # print(cursor.rowcount)
    # sql="SELECT * FROM user where username=%s && password=%s"
    # sql = "SELECT * FROM user where username=%s || password=%s"
    # sql = "SELECT * FROM user where username!=%s"
    # cursor.execute(sql)
    # print(cursor.rowcount)
    # sql = "UPDATE user SET username=%s WHERE username=%s"
    # newUsername = "张三" + str(random.randint(1, 10000))
    # print(newUsername)
    # data = (newUsername, "张三")
    # cursor.execute(sql, data)
    # conn.commit()
    return render(request, "acticle/list.html")


def listyer(request):
    _title = request.GET.get("num")
    print(_title)
    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='blog',  ##数据库名
        charset='utf8'  ##连接编码
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    _title = request.GET.get("num")
    print(_title)
    sql1 = "SELECT * FROM articlecontent WHERE aid=%s"
    # # cursor执行sql语句
    data1 = (_title)
    cursor.execute(sql1, data1)
    conn.commit()
    aa = cursor.fetchall()
    print(aa)
    # sql = "select * from articlecontent,article where article.id= articlecontent.aid;"
    # cursor.execute(sql)
    # rr1 = cursor.fetchall()
    # print(rr1)
    # return render(request, "acticle/listyer.html")
    return render_to_response('acticle/listyer.html', {'current_date': aa})




























