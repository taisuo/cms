from django.shortcuts import render
from django.template import  loader
# Create your views here.
from django.http import HttpResponse
from django.core import serializers
import math

import  pymysql
import json
from  datetime import datetime
from common import utils
from django.forms import forms
from DjangoUeditor.forms import  UEditorField
from index.models import *
class TestUEditorForm(forms.Form):
    content = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="static/images/", filePath="static/files/",
                          upload_settings={"imageMaxSize":1204000},
                          settings={})

def index(request):
    # return HttpResponse("Hello")
    return render(request,"server/index.html")
def indexHandle(request):
    list = serializers.serialize("json",inmenu.objects.filter(mecatid=1))
    print(list)
    return HttpResponse(utils.returnResult(1, "用户名不存",list))
def content(request):
    form=TestUEditorForm()
    print(form)
    listinfo = inmenu.objects.all()
    return render(request, "server/content.html",{"form":form,"listinfo":listinfo})
def contentHandle(request):
    title=request.POST.get("title")
    colorlist = request.POST.get("colorlist")
    num = request.POST.get("num")
    content = request.POST.get("content")
    headImg = request.FILES.get("headImg")
    content1 = request.POST.get("content1")
    print(content1)
    print(title,colorlist,num,headImg,content)
    size=getsize(headImg.size)
    if size>100:
        print("文件过大")
    type=headImg.name.split(".")[-1]
    print(type)
    if type not in ["jpg","png","jpeg","gif","bmp"]:
        print("类型错误")
    timestamp=int(datetime.now().timestamp()*1000000)
    print(timestamp)
    timenum=datetime.now()
    newsname="head"+str(timestamp)+"."+type
    print(newsname)
    imgpath="static/uploads/"+newsname
    with open(imgpath, 'wb') as f:
        for file in headImg.chunks():
            f.write(file)
            f.flush()

    newscontent = innews_content(newsid=1,content=content,newstime=timenum)
    newscontent.save()
    # list=innews_content.objects.all().values("id")
    list=innews_content.objects.filter(content=content).order_by('-id')
    for item in list:
         cat=item.id

    newarticle = news(title=title,title_font_colour=colorlist, thumb= newsname, num=num,catid=cat)
    newarticle.save()

    return HttpResponse(utils.returnResult(0, "发布成功"))
        # if userinfo:
        #     print("用户名存在")
        #     if pwd == userinfo["password"]:
        #         response = HttpResponse(utils.returnResult(0, "登录成功", {"uid": userinfo["id"]}))
        #         response.set_cookie("uid", userinfo["id"], max_age=60 * 60 * 24 * 3)
        #         return response
        #     return HttpResponse(utils.returnResult(1, "密码失败"))
        # else:
        #     print("用户名不存")
        #     return HttpResponse(utils.returnResult(1, "用户名不存"))

def addcontentlist(request):
    list = inmenu.objects.filter(mecatid="0")

    return render(request, "server/menulist.html",{"list":list})
def addcontent(request):
    list = inmenu.objects.filter(mecatid="0")

    return render(request, "server/addcontent.html",{"list":list})
def delcontentHandle(request):
    id = request.GET.get("uid")
    print(id)
    news.objects.filter(id=id).delete()
    innews_content.objects.filter(newsid=id).delete()
    return HttpResponse(utils.returnResult(0, "删除成功"))
def getsize(size, format = 'kb'):
    p = 0
    if format == 'kb':
        p = 1
    elif format == 'mb':
        p = 2
    elif format == 'gb':
        p = 3

    size /= math.pow(1024, p)

    return float("%0.2f"%size)
def contentlist(request):
    # return HttpResponse("Hello")
    num=request.GET.get("num")

    if num==None:
        num1=0
        num2=3
    else:
        num1 = 3*(int(num)-1)
        num2 = 3*int(num)
    list=news.objects.filter()[num1:num2]
    list2 = math.ceil(news.objects.filter().count()/3)
    print(list2)
    list1 = inmenu.objects.filter(mecatid="0")
    return render(request,"server/contentlist.html",{"list":list,"list1":list1,"numlist":list2})
def selectcontentHandle(request):
    uid = request.GET.get("uid")
    uid1 = request.GET.get("uid1")
    print(uid,uid1)
    list = news.objects.filter(title__contains=uid,num=uid1)
    print(list)
    return render(request, "server/contentlist.html", {"list": list})
def btnclickaddHandle(request):
    uid = request.GET.get("uid")
    uid1 = request.GET.get("uid1")
    print(eval(uid))
    for i in eval(uid):
        print(i)
    news.objects.filter(id__in=eval(uid)).update(num=uid1)
    return HttpResponse(utils.returnResult(0, "发布成功"))
def menu(request):
    return render(request, "server/menu.html")
def menuHandle(request):
    menutitle = request.POST.get("menutitle")
    menuaddnum = request.POST.get("menuadd")
    radionum = request.POST.get("radionum")
    print(menutitle,radionum)
    newscontent = inmenu(menuname=menutitle,mecatid=radionum,menuadd=menuaddnum)
    newscontent.save()
    return HttpResponse(utils.returnResult(0, "发布成功"))
def menulist(request):
    list = inmenu.objects.all()

    return render(request, "server/menulist.html",{"list":list})
def delmenuHandle(request):
    id = request.GET.get("uid")
    print(id)
    inmenu.objects.filter(id=id).delete()

    return HttpResponse(utils.returnResult(0, "删除成功"))
def recommend(request):

    return render(request, "server/recommend.html", {"list": list})
def recommendHandle(request):
    menutitle = request.POST.get("menutitle")
    recomtitle = request.POST.get("recomtitle")
    radionum = request.POST.get("radionum")
    print(menutitle, recomtitle, radionum)
    timenum = datetime.now()
    inposition = inposition_content(content=menutitle,newsid=radionum ,createttime=timenum )
    inposition.save()
    return HttpResponse(utils.returnResult(0, "发布成功"))
def recommendlist(request):
    list=inposition_content.objects.filter()
    return render(request, "server/recommendlist.html", {"list": list})
def delrecommendHandle(request):
    id = request.GET.get("uid")
    print(id)
    inposition_content.objects.filter(id=id).delete()

    return HttpResponse(utils.returnResult(0, "删除成功"))
def addrecommendlist(request):

    return render(request, "server/addrecommendlist.html")
def addrecommendlistHandle(request):
    print(122)
    id = request.GET.get("uid")
    print(id)
    list = serializers.serialize("json",inposition_content.objects.filter(id=id))
    print(list)
    return HttpResponse(utils.returnResult(0, "1111",list))
def admin(request):
    form = TestUEditorForm()
    return render(request, "server/admin.html",{"form":form})
def adminHandle(request):
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    email = request.POST.get("email")
    content1 = request.POST.get("content1")
    content = request.POST.get("content")
    newtime=datetime.now()
    headImg = request.FILES.get("headImg")
    size = getsize(headImg.size)
    if size > 100:
        print("文件过大")
    type = headImg.name.split(".")[-1]
    print(type)
    if type not in ["jpg", "png", "jpeg", "gif", "bmp"]:
        print("类型错误")
    timestamp = int(datetime.now().timestamp() * 1000000)
    print(timestamp)
    timenum = datetime.now()
    newsname = "head" + str(timestamp) + "." + type
    print(newsname)
    imgpath = "static/uploads/" + newsname
    with open(imgpath, 'wb') as f:
        for file in headImg.chunks():
            f.write(file)
            f.flush()

    print(username,pwd,email,content1,content)

    user = inadmin(username=username,password=pwd,email=email,content=content,registtime=newtime,images=newsname)
    user.save()
    return HttpResponse(utils.returnResult(0, "注册成功"))

def adminlist(request):
    user=inadmin.objects.all()
    return render(request, "server/adminlist.html",{"user":user})
def deladminHandle(request):
    id = request.GET.get("uid")
    print(id)
    inadmin.objects.filter(id=id).delete()

    return HttpResponse(utils.returnResult(0, "删除成功"))
def login(request):
    return render(request, "server/login.html", {"list": list})
def loginHandle(request):
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    email = request.POST.get("email")
    print(username,pwd,email)
    # return HttpResponse(utils.returnResult(0, "登录成功"))
    # userinfo=inadmin.objects.get(username=username)
    # print( userinfo.username)
    try:
        userinfo = inadmin.objects.get(username=username)
    except:
        userinfo=None
    print(userinfo)
    if userinfo:
        print("用户名存在")
        if pwd==userinfo.password:
            response=HttpResponse(utils.returnResult(0, "登录成功"))
            response.set_cookie("uid",userinfo.username,max_age=60*60*24*3)
            return response
        return HttpResponse(utils.returnResult(1, "密码失败"))
    else:
        print("用户名不存")
        return HttpResponse(utils.returnResult(1, "用户名不存"))
def delHandle(request):
    uid=request.GET.get("uid")
    print(uid)
    response = response=HttpResponse(utils.returnResult(0, "ok"))
    response.delete_cookie('uid')
    return response
