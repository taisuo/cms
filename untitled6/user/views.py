from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here
import json
import pymysql
def regist(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "user/regist.html")
def registHangle(request):
    _username = request.POST.get("username")
    _pwd = request.POST.get("pwd")
    _email= request.POST.get("email")
    dic = {
        "code": 0,
        "msg": "注册成功",
    }
    dic1 = json.dumps(dic)
    return HttpResponse(dic1)
def login(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "user/login.html")