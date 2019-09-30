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
    pwd = request.POST.get("pwd")
    email = request.POST.get("email")
    print(username)
    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='user1',  ##数据库名
        charset='utf8'  ##连接编码
    )
    now = datetime.now()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "INSERT INTO userlist(username,pwd,email,registtime)values ('%s','%s','%s','%s')"

    print(sql)
    data = (username, pwd, email, now)
    cursor.execute(sql % data)
    conn.commit()

    # return HttpResponse(username+pwd)
    dic = {
        "code": 0,
        "msg": "注册成功",
        }
    dic1=json.dumps(dic)
    return HttpResponse(dic1)

def login(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "user/login.html")
def loginHandle(request):
    username=request.POST.get("username")
    pwd = request.POST.get("pwd")
    email = request.POST.get("email")
    # return HttpResponse(username+pwd)
    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='123456',  ##密码
        db='user1',  ##数据库名
        charset='utf8'  ##连接编码
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from userlist where username= %s &&pwd=%s"
    data = ( username,pwd)
    cursor.execute(sql, data)
    print(cursor.rowcount)
    if(cursor.rowcount<0):
        dic = {
            "code": 0,
            "msg": "注册成功",
        }
        dic1 = json.dumps(dic)
        return HttpResponse(dic1)