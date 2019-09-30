from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse         #需要导入HttpResponse模块

#def index(request):    #request参数必须有，它封装了用户请求的所有内容
    #return HttpResponse("Hello ")    #不能直接字符串，必须是由这个类封装，此为Django规则

def index(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容

    response = HttpResponse("hello")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def index1(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容

    response = HttpResponse("hello-----")
    response["Access-Control-Allow-Origin"] = "*"
    return response
def index2(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.POST.get('city')
    if username == "北京":  # 判断num的值
        response = HttpResponse("post---北京是首都")
    elif username == "上海":
        response = HttpResponse("post---上海是魔都")
    else:
        response = HttpResponse("post---其他城市")
    response["Access-Control-Allow-Origin"] = "*"

    return response
def index3(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.GET.get('code')
    if username == "1":  # 判断num的值
        response = HttpResponse("post---北京是首都")
    elif username == "2":
        response = HttpResponse("post---上海是魔都")
    else:
        response = HttpResponse("post---其他城市")
    response["Access-Control-Allow-Origin"] = "*"

    return response
def index4(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容

    response = HttpResponse('<root><li url="1.jpg">图片1</li><li url="2.jpg">图片2</li><li url="3.jpg">图片3</li><li url="4.jpg">图片4</li><li url="5.jpg">图片5</li></root>',content_type="text/xml")
    response["Access-Control-Allow-Origin"] = "*"
    return response
def index8(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.GET.get('id')
    if username == "0":  # 判断num的值
        response = HttpResponse('[{"title":"新闻1","id":0},{"title":"新闻2","id":1},{"title":"新闻3","id":2}]')
    elif username == "1":
        response = HttpResponse('[{"img":"1.jpg","title":"图片1","id":3},{"img":"2.jpg","title":"图片2","id":4},{"img":"3.jpg","title":"图片3","id":5}]')
    else:
        response = HttpResponse('[{"title":"航空新闻1","id":6},{"title":"航空新闻2","id":7},{"title":"航空新闻3","id":8}]')

    response["Access-Control-Allow-Origin"] = "*"
    return response
def index9(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.GET.get('big')
    idname=request.GET.get('id')
    if (username == "0" and idname=="1"):  # 判断num的值
        response = HttpResponse('{"title":"新闻1","time":"2018-10-21","content":"新闻内容","writer":"QQ群"}')
    elif (username == "0" and idname=="2"):
        response = HttpResponse('{"title":"新闻2","time":"2018-10-22","content":"我是好人","writer":"一样"}')
    elif (username == "0" and idname == "3"):
        response = HttpResponse('{"title":"新闻2","time":"2018-10-22","content":"我是好人","writer":"一样"}')
    elif (username == "2" and idname == "1"):
        response = HttpResponse('{"title":"航空军事新闻1","time":"2018-10-24","content":"我是好人","writer":"1"}')
    elif (username == "2" and idname == "2"):
        response = HttpResponse('{"title":"航空军事新闻2","time":"2018-10-24","content":"我是好人","writer":"2"}')
    elif (username == "2" and idname == "3"):
        response = HttpResponse('{"title":"航空军事新闻3","time":"2018-10-24","content":"我是好人","writer":"3"}')
    else:
        response = HttpResponse("post---其他城市")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def index10(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.GET.get('city')
    if username == "0":  # 判断num的值
        response = HttpResponse('{"title":"图片1","time":"2018-10-21","content":"我是好人","img":"1.jpg","writer":"1"}')
    elif username == "1":
        response = HttpResponse('{"title":"图片2","time":"2018-10-21","content":"我是好人","img":"2.jpg","writer":"2"}')
    else:
        response = HttpResponse('{"title":"图片3","time":"2018-10-21","content":"我是好人","img":"3.jpg","writer":"3"}')

    response["Access-Control-Allow-Origin"] = "*"
    return response
def index11(request, response=None):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    username = request.GET.get('id')
    if username == "0":  # 判断num的值
        response = HttpResponse('{"title":"图片0","time":"2018-10-21","content":"我是好人","img":"1.jpg","writer":"1"}')
    elif username == "1":
        response = HttpResponse('{"title":"图片1","time":"2018-10-21","content":"我是好人","img":"2.jpg","writer":"2"}')
    elif username == "2":
        response = HttpResponse('{"title":"图片2","time":"2018-10-21","content":"我是好人","img":"2.jpg","writer":"2"}')
    elif username == "3":
        response = HttpResponse('{"title":"图片3","time":"2018-10-21","content":"我是好人","img":"2.jpg","writer":"2"}')
    elif username == "4":
        response = HttpResponse('{"title":"图片4","time":"2018-10-21","content":"我是好人","img":"2.jpg","writer":"2"}')
    elif username == "5":
        response = HttpResponse('{"title":"图片5","time":"2018-10-21","content":"我是好人","img":"2.jpg","writer":"2"}')
    elif username == "6":
        response = HttpResponse('{"title":"图片6","time":"2018-10-21","content":"我是好人","img":"2.jpg","writer":"2"}')
    elif username == "7":
        response = HttpResponse('{"title":"图片7","time":"2018-10-21","content":"我是好人","img":"2.jpg","writer":"2"}')
    else:
        response = HttpResponse('{"title":"图片8","time":"2018-10-21","content":"我是好人","img":"3.jpg","writer":"3"}')
    response["Access-Control-Allow-Origin"] = "*"
    return response