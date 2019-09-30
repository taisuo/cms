from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template=loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,request))

def register(request):
    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context, request))
def login(request):
    if request.method=='POST':
        u = request.POST['user']
        p = request.POST['pwd']
        print(u, p)

    template = loader.get_template('login.html')
    context = {}
    # return HttpResponse(template.render(context, request))
    return render(request,'login.html')
def list(request):
    template = loader.get_template('list.html')
    context = {}
    return HttpResponse(template.render(context, request))
def add(request):
    template = loader.get_template('add.html')
    context = {}
    return HttpResponse(template.render(context, request))