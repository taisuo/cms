"""
WSGI config for untitled8 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import random
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled8.settings')

application = get_wsgi_application()
print(os.name)
# os.system(cmd)
# reault=os.popen(cmd)
# result.read()
# print(os.listdir("c:"))
# print(os.chdir(".."))
# print(os.getcwd)
# print(os.mkdir("test"))
# os.remove('myapp.log')
# os.rmdir("test")
# os.rename("demom1.py","demon11.py")
# os.linesep
# if not os path.exists('text'):
#     os.path.splitp
# os.path.abspath("/")
# os.path.aplit() 分割线
# import sys
# f=open("log.txt",a)
# __console__=sys.stdout
# sys.stdout=f
# print('hello python')
# sys.stdoudt=__console__
# print("hellow orld")
# sys.exit(n)
# import random
# print(random.randrange(1,1000))
# print(random.sample([1,2,3,4],2))
import string
# print(string.ascii_letter)
# string.digits
# string.ascii_lowercase
# string.ascii_uppercase
# string.printable
# from io import StringIO
# stringIO=StringIO()
# stringIO.write("hello world")
# stringIO.write("uio")
# import json
# dic={"k1":"v1","k2":"v2","k3":"v3"}
# str_dic=json.dumps(dic)
# print(type(str_dic),str_dic)
# dic2=json.load(str_dic)
# list_dic=[1,["a","b","c"],3,{"k1":"v1","k2":"v2"}]
# str_dic=json.dumps(list_dic)
# print(type(str_dic),str_dic)
# list_dic2=json.loads(str_dic)
# print(type(list_dic2),list_dic2)
from datetime import datetime,date,timedelta
now=date.today()
print(now)
print(now.strftime("%Y.%m.%d"))
print(now.strftime('%Y{}%m{}%d{}').format("年","月","日"))
birthday=date(2000,1,1)
print(birthday)
age=now-birthday
print(age)
print(age.days)
now = datetime.now()
print(now)
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
dt = datetime(2015, 4, 19, 12, 20)
dt.timestamp()
ts=dt.timestamp()
print(ts)
t = 1429417200.0
print(datetime.fromtimestamp(t))
t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
time1 = datetime.now()
print(time1)
print(time1.strftime("%y-%m-%d %H:%M:%S"))
print((time1+timedelta(hours =1)).strftime("%y-%m-%d %H:%M:%S"))
print((time1+timedelta(days =1)).strftime("%y-%m-%d %H:%M:%S"));
print((time1+timedelta(days=2,hours =1)).strftime("%y-%m-%d %H:%M:%S"))
now=date.today()
print(now)
print(now.strftime("%Y.%m.%d"))
print(now.strftime('%Y{}%m{}%d{}').format("年","月","日"))
birthday=date(2000,1,1)
print(birthday)
age=now-birthday
print(age)
print(age.days)
now = datetime.now()
print(now)
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
dt = datetime(2015, 4, 19, 12, 20)
dt.timestamp()
ts=dt.timestamp()
print(ts)
t = 1429417200.0
print(datetime.fromtimestamp(t))
t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
time1=datetime.now()
print(time1)
print(time1)
print(time1.strftime("%y-%m-%d %H:%M:%S"))
print((time1+timedelta(hours =1)).strftime("%y-%m-%d %H:%M:%S"))
print((time1+timedelta(days =1)).strftime("%y-%m-%d %H:%M:%S"));
print((time1+timedelta(days=2,hours =1)).strftime("%y-%m-%d %H:%M:%S"))































