from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
import  pymysql
from . import module
from datetime import datetime
from common import utils
from common import db

def regist(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
     return  render(request,"user/regist.html")
def registHangle(request):
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    email = request.POST.get("email")
    print(username,pwd,email)
    now=datetime.now()
    print(now)
    sql="SELECT * FROM user WHERE username=%s"
    data=(username)

    # db.Db.cursor.execute(sql, data)
    # userinfo=db.Db.cursor.fetchone()
    # print(userinfo)
    userinfo=db.Db.select(sql,0,data)
    if userinfo=="error":
        return HttpResponse(utils.returnResult(1, "用户名已存在"))
    else:
        return HttpResponse(utils.returnResult(1, "用户名已存在"))
    if(userinfo):
        print("用户存在")
        return HttpResponse(utils.returnResult(1, "用户名已存在"))

    keyvalue="username,password,registtime"
    value="%s,%s,%s"
    data = (username, pwd,datetime.now())
    print(data)
    if(email):
        print("邮箱存在")
        keyvalue+=",email"
        value+=",%s"
        data = (username, pwd, datetime.now(), email)
    sql="INSERT INTO user("+keyvalue+") values("+value+")"
    print(sql)

    try:
        db.Db.cursor.execute(sql, data)
        db.Db.conn.commit()
        return HttpResponse(utils.returnResult(0, "注册成功"))
    except Exception as e:
        return HttpResponse(utils.returnResult(1, "注册失败"))
def login(request):
    return render(request, "user/login.html")

def loginHangle(request):
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    print(username,pwd)
    sql="SELECT id,password FROM user WHERE username= %s"
    data=username
    db.Db.cursor.execute(sql, data)
    userinfo = db.Db.cursor.fetchone()
    print( userinfo)
    if userinfo:
        print("用户名存在")
        if pwd==userinfo["password"]:
            response=HttpResponse(utils.returnResult(0, "登录成功",{"uid":userinfo["id"]}))
            response.set_cookie("uid",userinfo["id"],max_age=60*60*24*3)
            return response
        return HttpResponse(utils.returnResult(1, "密码失败"))
    else:
        print("用户名不存")
        return HttpResponse(utils.returnResult(1, "用户名不存"))
















