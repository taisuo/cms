from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import json
import  pymysql
from datetime import datetime
from common import db
from common import utils


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)


def list(request):
    uid=request.COOKIES["uid"]
    sql = "SELECT * FROM article WHERE uid=%s"
    data = uid
    db.Db.cursor.execute(sql, data)
    userinfo = db.Db.cursor.fetchall()
   # return  HttpResponse("123456")
    return render(request, "article/list.html",{"articlelist":userinfo})
def getArticleList(request):
    uid=request.GET.get("uid")
    print(uid)
    sql="SELECT id,title,uid FROM article WHERE uid=%s"
    data=uid
    db.Db.cursor.execute(sql,data)
    userinfo = db.Db.cursor.fetchall()
    print(userinfo)
    return HttpResponse(utils.returnResult(0, "", userinfo))
def addArticle(request):
    return render(request, "article/addArticle.html")
def addArticleHangle(request):
    '''添加处理页面'''
    title = request.POST.get("title")
    uid = request.POST.get("uid")
    content = request.POST.get("content")
    print(title,uid,content)
    sql="INSERT INTO article(title,uid) VALUES (%s,%s)"
    data=(title,uid)
    db.Db.cursor.execute(sql,data)
    insertid=db.Db.conn.insert_id()
    print(insertid)
    sql="INSERT INTO articlecontent(aid,content) VALUES (%s,%s)"
    data = (insertid,content)
    db.Db.cursor.execute(sql,data)
    db.Db.conn.commit()
    return HttpResponse(utils.returnResult(0, "发布成功"))

def articleDite(request):
    return render(request, "article/articleDite.html")
def getusername(request):
    '''uid换取数据'''
    uid=request.GET.get("uid")
    print(uid)
    sql="SELECT username  FROM user WHERE id= %s "
    data=uid
    db.Db.cursor.execute(sql,data)
    userinfo = db.Db.cursor.fetchone()
    print(userinfo)
    return HttpResponse(utils.returnResult(0, "",userinfo))

def getarticleDiteinfo(request):
    id = 1
    sql="SELECT * FROM articlecontent WHERE aid= %s"
    data=id
    db.Db.cursor.execute(sql,data)
    userinfo = db.Db.cursor.fetchone()
    print(userinfo)
    return HttpResponse(utils.returnResult(0, "", userinfo))








