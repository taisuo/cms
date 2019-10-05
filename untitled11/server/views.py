from django.shortcuts import render
from django.template import  loader
# Create your views here.
from django.http import HttpResponse
import math
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
def content(request):
    form=TestUEditorForm()
    print(form)
    return render(request, "server/content.html",{"form":form})
def contentHandle(request):
    title=request.POST.get("title")
    colorlist = request.POST.get("colorlist")
    num = request.POST.get("num")
    content = request.POST.get("content")
    headImg = request.FILES.get("headImg")
    id_content = request.POST.get("id_content")
    print(id_content)
    print(title,colorlist,num,headImg)
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
    list=innews_content.objects.all().values("id")
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

    return render(request,"server/contentlist.html")
def menu(request):
    return render(request, "server/menu.html")
def menuHandle(request):
    menutitle = request.POST.get("menutitle")
    radionum = request.POST.get("radionum")
    print(menutitle,radionum)
    newscontent = inmenu(menuname=menutitle,mecatid=radionum)
    newscontent.save()
    return HttpResponse(utils.returnResult(0, "发布成功"))
def menulist(request):
    list = inmenu.objects.all()
    list1 = inmenu.objects.filter(mecatid="0")
    print(list1)
    return render(request, "server/menulist.html",{"list":list})