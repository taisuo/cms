from django.shortcuts import render
from django.http import HttpResponse         #需要导入HttpResponse模块
from django.shortcuts import render
from urllib import parse
from urllib.request import urlopen
import zlib
import importlib
from urllib.parse import quote
import string
from django.http import HttpResponse         #需要导入HttpResponse模块
from django.http import HttpResponse         #需要导入HttpResponse模块
# Create your views here.
def index(request):    #request参数必须有，它封装了用户请求的所有内容
    return HttpResponse("Hello---------123 ")    #不能直接字符串，必须是由这个类封装，此为Django规则

def getContent(request):
    filename="data.txt"
    url = request.POST.get('url')
    # url = 'http://ws.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?UserID=&TrainCode=1461'
    #url = 'http://ws.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getStationAndTimeByStationName?UserID=5108d99f5719441da74cf16c83052544&StartStation=北京&ArriveStation=上海'
    url = quote(url, safe=string.printable)
    r=urlopen(url)
    content=r.read().decode('utf-8', 'ignore').replace(u'\xa9', u'')
    with open('data.txt', 'w',encoding="utf-8") as f:  # 设置文件对象
        f.write(content)
    fp = open(filename, "r", encoding="utf-8")

    str=fp.read()

    response = HttpResponse(str,content_type="text/xml")
    response["Access-Control-Allow-Origin"] = "*"

    return response  # 不能直接字符串，必须是由这个类封装，此为Django规则
def index8(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.GET.get('user')
    pwd=request.GET.get('pwd')
    if username == "张三" and pwd=="123":  # 判断num的值
        response = HttpResponse('0')
    elif username == "张三" and pwd!="123":
        response = HttpResponse('1')
    else:
        response = HttpResponse('2')

    response["Access-Control-Allow-Origin"] = "*"

    return response

def index9(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.GET.get('user')

    if username == "first":  # 判断num的值
        response = HttpResponse('["娱乐新闻1","娱乐新闻2","娱乐新闻3"]')
    elif username == "sec":
        response = HttpResponse('["财经新闻1","财经新闻2","财经新闻3"]')
    else:
        response = HttpResponse('"没有数据"')

    response["Access-Control-Allow-Origin"] = "*"

    return response


def index10(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.POST.get('id')

    if username == "1":  # 判断num的值
        response = HttpResponse('[{"name":"商品1-1","price":100,"img":"001.png"},{"name":"商品1-2","price":100,"img":"002.jpg"},{"name":"商品1-3","price":100,"img":"003.png"}]')
    elif username == "2":
        response = HttpResponse('[{"name":"商品2-1","price":100,"img":"001.png"},{"name":"商品2-2","price":100,"img":"002.jpg"},{"name":"商品2-3","price":100,"img":"003.png"}]')
    elif username == "3":
        response = HttpResponse('[{"name":"商品3-1","price":100,"img":"001.png"},{"name":"商品3-2","price":100,"img":"002.jpg"},{"name":"商品3-3","price":100,"img":"003.png"}]')
    elif username == "4":
        response = HttpResponse('"数据4"')
    elif username == "5":
        response = HttpResponse('"数据5"')
    elif username == "6":
        response = HttpResponse('"数据6"')
    elif username == "7":
        response = HttpResponse('"数据7"')
    elif username == "8":
        response = HttpResponse('"数据8"')
    elif username == "9":
         response = HttpResponse('"数据9"')
    else:
        response = HttpResponse('"没有数据"')

    response["Access-Control-Allow-Origin"] = "*"

    return response

def index11(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.GET.get('id')

    if username == "1":  # 判断num的值
        response = HttpResponse('[{"name":"商品1","price":100,"img":"001.png"},{"name":"商品2","price":100,"img":"002.jpg"},{"name":"商品3","price":100,"img":"003.png"}]')
    elif username == "2":
        response = HttpResponse('"数据2"')

    else:
        response = HttpResponse('"没有数据"')

    response["Access-Control-Allow-Origin"] = "*"

    return response