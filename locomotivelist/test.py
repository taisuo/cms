# import test1 #导入文件的时候已经把python文件执行了一次,打印出python
# print(test1.name) #打印出hello
# test1.my() #打印出python
# from test1 import name,my #这种调用自定义函数时不用再写“文件名.函数”，直接写函数或者变量名
# print(name)
# my()

# from test1 import * #导入所有的
# #from aa import *
# print(name)
# my()
# import sys
# print(sys.path)
# import os
# print(os.name)
# if os.name == "nt":
#     cmd = "ipconfig"
# elif os.name == "posix":
#     cmd = "ifconfig"
# os.system(cmd)
# os.system(cmd)
# result = os.popen(cmd)
# result.read()
# os.listdir("G:")
# os.chdir("..")
# os.getcwd
# os.mkdir("AAAA")
# os.remove("myapp.log")
# os.rmdir("test")
#
# import sys
# f = open('log.txt','a')   #以追加的模式打开一个文件
# __console__ = sys.stdout   #备份默认console命令行
# sys.stdout = f   #指定标准输出到文件
# print('hello python')
# sys.stdout = __console__  #将标准输出改为模式的console命令行模式
# print('hello world')    #输出将会在console命令行下


# import random
# print(random.randrange(1,100))
# print(random.sample([1, 2, 3, 4, 5, 6, 7], 3))
#
#
# class NumberCount(object):
#     def __init__(self):
#         self.number1 = 0
#         self.number2 = 0
#         self.number3 = 0
#         self.number4 = 0
#         self.number5 = 0
#         self.number6 = 0
#     def count(self):
#         for i in range(1, 6001):
#             number = random.randint(1, 6)
#             if number == 1:
#                 self.number1 += 1
#             if number == 2:
#                 self.number2 += 1
#             if number == 3:
#                 self.number3 += 1
#             if number == 4:
#                 self.number4 += 1
#             if number == 5:
#                 self.number5 += 1
#             if number == 6:
#                 self.number6 += 1
#     def getResult(self):
#         print("1出现的次数: {0}".format(self.number1))
#         print("2出现的次数: {0}".format(self.number2))
#         print("3出现的次数: {0}".format(self.number3))
#         print("4出现的次数: {0}".format(self.number4))
#         print("5出现的次数: {0}".format(self.number5))
#         print("6出现的次数: {0}".format(self.number6))
# if __name__ == "__main__":
#     numberCount = NumberCount()
#     numberCount.count()
#     numberCount.getResult()
# import re
# print(re.findall(r"123","123456"))
# import sys
# print(sys.path)
# import random
# ret=random.random()
# print(ret)
# print ("random() : ",random.random())
# print ("random() : ",random.random())
# print(random.uniform(1,10))
# print(random.uniform(10,1))
# print(random.randint(1,9))
# print(random.randrange(10,30,3))
# lst = ['python','C','C++','javascript']
# str1 = ('I love python')
# print(random.choice(lst))
# print(random.choice(str1))
# p = ['A' , 'B', 'C', 'D', 'E' ]
# random.shuffle(p)
# print (p)
# lst = [1,2,3,4,5]
# print(random.sample(lst,2))
# print(lst)
# import os
# print(os.access('G:\pythonwork\server\locomotivelist\test.py',os.F_OK))
# print(os.getcwd())
# os.chdir(G:\\pythonwork\\server\\locomotivelist\\aaa')
# print(os.getcwd())
# print(sys.version)
# print(sys.platform)
# print(sys.stdout)
# import time,sys
# for i in range(20):
#     sys.stdout.write("=")
#     time.sleep(0.5)
#     sys.stdout.flush() #从缓存刷新的屏幕
# import sys
# my_sys = sys.argv
# for i in my_sys:
#     print(i)
import random
import  string
print(string.ascii_letters)
print(string.digits)
print(random.sample(str(string.digits),2))
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.printable)
print(string.punctuation)
print(string.hexdigits)
print("".join(random.sample(string.ascii_letters + string.digits, 4)))













