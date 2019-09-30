from django.shortcuts import render,HttpResponse
import time,datetime

# Create your views here.
def show_time(request):
    t=datetime.datetime.now()
    # return HttpResponse("<html><body>It is now %s.</body></html>" % t)
    # return render(request,"show_time.html",{"time":t})



def query(request):
    l=["春章","发动机号","回复"]
    d={"name":"建委","age":"12"}
    # return render(request, "index.html", {"action": l})
    return render(request, "index.html", locals())