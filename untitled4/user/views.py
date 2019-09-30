from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here
import json
import pymysql
def regist(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "user/regist.html")
def registHandle(request):
    username=request.POST.get("username")
    print(username)
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
    # 用户名存在
    sql = "SELECT * FROM user WHERE username=%s"
    print(now)
    _username = request.POST.get("username")
    _pwd = request.POST.get("pwd")
    data = (_username)
    print(data)
    cursor.execute(sql, data)
    conn.commit()
    print(cursor.rowcount)
    if (cursor.rowcount > 0):
        dic = {
            "code": 1,
            "msg": "用户名存在",
        }
        dic1 = json.dumps(dic)
        return HttpResponse(dic1)
    # 用户名不存在
    _email = request.POST.get("email")
    if(_email!=""):
        print('email存在')
        sql = "INSERT INTO user(username,password,email,registtime)values (%s,%s,%s,%s)"
        data = (_username, _pwd, _email, now)
        cursor.execute(sql,data)
        conn.commit()
        dic = {
            "code": 0,
            "msg": "注册成功",
        }
        dic1 = json.dumps(dic)
        return HttpResponse(dic1)

    else:
        print('email不存在')
        sql = "INSERT INTO user(username,password,registtime)values (%s,%s,%s)"
        data = (_username, _pwd, now)
        cursor.execute(sql,data)
        conn.commit()
        dic = {
            "code": 0,
            "msg": "注册成功",
        }
        dic1 = json.dumps(dic)
        return HttpResponse(dic1)




    # return HttpResponse(username+pwd)


def login(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "user/login.html")
def loginHandle(request):
    _username=request.POST.get("username")
    _pwd = request.POST.get("pwd")
    _email = request.POST.get("email")
    # return HttpResponse(username+pwd)
    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='blog',  ##数据库名
        charset='utf8'  ##连接编码
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #用户名存在
    sql = "select id from user where username= %s and password=%s"
    data = (_username,_pwd)
    cursor.execute(sql, data)
    print(cursor.rowcount)
    rs = cursor.fetchone()
    print(rs)
    if(cursor.rowcount>0):
        dic = {
            "code": 0,
            "msg": "登录成功",
        }
        dic.setdefault("uid",rs["id"])
        print(dic)
        dic1 = json.dumps(dic)
        return HttpResponse(dic1)
    # 用户名不存在
    dic = {
        "code": 1,
        "msg": "登录不成功",
    }
    dic1 = json.dumps(dic)
    return HttpResponse(dic1)