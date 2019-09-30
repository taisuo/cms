from django.shortcuts import render,HttpResponse

# Create your views here.
from django.http import HttpResponse,requset
from django.template import loader
import time
def index(requset):
    t=time.ctime()
    # return HttpResponse("Hello, world. You're at the polls index.")
    # template=loader.get_template('polls/index.html')
    # context={}
    # return HttpResponse(template.render(context,request))
    return render(requset,"polls/index.html",{"time":t})
def register(requset):
    # print(request.GET.get("user"))
    # print(request.GET.get("age"))
    # if request.method=="GET":
    #     user=request.GET.get("user")
    #     if user=="yuan":
    #          return redirect("/lodin/")
    #     else:
    #           return HttpResponse("success!")
    return render(requset,"polls/register.html")
def login(requset):
    return render(requset, "polls/login.html")









































