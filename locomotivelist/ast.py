#name="zhangsan"
#name = input("请输入用户名：")
#print(name)
#name = input("What is your name?")
#age = input("How old are you?")
#hometown = input("Where is your hometown?")
#print(age)
#a = 123
#print(type(a))
#print(1.25*100)
#print(type(12.5*10))
#name = "bingbing fan"
#print(type(name))
#msg = '''My name is zhangsan, I am 22 years old!'''
#msg = "My name is Tom , I'm 22 years old!"
#msg = '''
#今天我想写首小诗，
#歌颂我的同桌，
#你看他那乌黑的短发，
#好像一只炸毛鸡。'''

#print(msg)
#name='Bingbing fan'

#print(name*10 )
# a=3
# b=5
# print(a<b)
#name = input("Name:")
#print("zhangsan")
#age = input("Age:")
#job = input("Job:")
#hobbie = input("Hobbie:")
#info = '''Name  : %s  #代表 name
#Age   : %s  #代表 age
#job   : %s  #代表 job
#Hobbie: %s  #代表 hobbie

#'''
#print(info)
#age = int(  input("Age:")  )print(type(age))
#print(age)
#msg = "我是%s,年龄%d,目前学习进度为80%%"%('金鑫',18)
#print(msg)
# age_of_jijuao = 48

# guess = int(input(">>:"))
# if guess > age_of_jijuao :
    # print("猜的太大了，往小里试试...")
# elif guess < age_of_jijuao :
    # print("猜的太小了，往大里试试...")
# else:
    # print("恭喜你，猜对了...")
# count = 0
# while count <= 10:
#     count += 1
#     if count == 11:count = 0
#     print("Loop",count)
# else:
#     print("循环正常执行完啦")
#     print("-----out of while loop ------")
# 求1-100的所有数的和
# x=1
# y=0
# while True:
#     y=y+x
#     if x==100:
#       break
#     x+=1
# print(y)

# start =1
# while start < 101:
#     temp = start % 2
#     if temp == 0:
#         print(start)
#     else:
#         pass
#     start += 1
#
# start =1
# while start < 101:
#     temp = start % 2
#     if temp == 1:
#         print(start)
#     else:
#         pass
#     start += 1
# start = 1
# sum = 0
# while start < 100:
#         temp = start % 2
#         if temp == 1:
#             sum = sum + start
#         else:
#             sum = sum - start
#         # print(start)
#         # sum = sum + 1
#         start += 1
# print(sum)

# i=0
# age=22
# while i < 3:
#     guss=int(input("猜谜"))
#     if guss == age:
#         print("在三次之内猜对了年龄!")
#     elif guss < age:
#         print("Too young")
#         i=i+1
#     elif guss > age:
#         print("Too old")
#         i+=1
#     elif i>=3:
#          print("次数用尽")
#          guss="123"
#          # break
# else:
#     print("次数用尽")
#     guss = "123"


"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
# print("123")
# name = input("What is your name?")
# age = input("How old are you?")
# hometown = input("Where is your hometown?")
# print("Hello ",name , "your are ", age , "years old, you came from",hometown)

# x = "a"
# y = "b"
# # 换行输出
# print(x);print(y)
#
#
# print('---------')
# # 不换行输出
# print(x, end=" ")
# print(y, end=" ")
# print()
# a = b = c = 1
# a, b, c = 1, 2, "runoob"
# print(a)
# print(b)
# print(c)
# a = 111
# isinstance(a, int)
# name = input("Name:")
# age = input("Age:")
# job = input("Job:")
# hobbie = input("Hobbie:")
#
# info = '''
# Name  : %s  #代表 name
# Age   : %s  #代表 age
# job   : %s  #代表 job
# Hobbie: %s  #代表 hobbie ------------- end -----------------''' %(name,age,job,hobbie)
# print(info)
#

# 8 or 4
# tu1 = ('a', 'b', '张三', 3, 666)
# print(tu1[0])  # 'a'
# print(tu1[-1])  # 666
# print(tu1[1:3])  # ('b', '张三')
# print(tu1[:-1])  # ('a', 'b', '张三', 3)
# print(tu1[::2])  # ('a', '张三', 666)
# print(tu1[::-1])  # (666, 3, '张三', 'b', 'a')

#
# tu1 = ('a', 'b', '张三', 3, 666)
# for i in tu1:
#     print(i)
# tu = ('张三', '张三', 'WuSir', '吴超')
# print(tu.count('张三')) # 2
# tu1 = (1,2,3,4,84,5,2,8,2,11,88,2)
# print(len(tu1))
# tup = ('Google', 'Runoob', 1997, 2000)
#
# print(tup)
# del tup;
# print("删除后的元组 tup : ")
# print(tup)
# li=["张三","李四","王五"]
# for i in li:
#  print(i)
#
# tup = ('Google', 'Runoob', 1997, 2000)
#
# for i in tup:
#     print(i)
# dic = {"name":"tanlaoshi","age":18,"sex":"girle"}
# for key in dic:
#     print(key)
# for item in dic.items():
#     print(item)
# for key,value in dic.items():
#     print(key,value)
# num=[];
# i=2
# for i in range(2,100):
#    j=2
#    for j in range(2,i):
#       if(i%j==0):
#          break
#    else:
#       num.append(i)
# print(num)
# for i in num:
#     print(i)
#
# dict = {'Name': '小学', 'time': 1989, 'sex': '7','site':{'state':'中国','city':'北京'}}
#
# for key,value in dict.items():
#    if key=="site" :
#        for key1,value1 in value.items():
#            print(value1)
#    else:
#        print(value)
#
# student_list = [{'name':'张三','sex':'男','age':'90','mark':'78'},
#                 {'name': '李四','sex':'男','age':'90','mark': '68'},
#                 {'name': '王五', 'sex':'男','age':'90','mark': '89'},
#                 {'name': '刘六','sex':'男','age':'90','mark': '79'},
#                 {'name': '钱七','sex':'男','age':'90','mark': '61'}]
#
# for i in range(len(student_list)):
#     print(student_list[i])
#     for key,value in student_list[i].items():
#         tup = ()=print(value)
#
#
#
# print(tup)


# a = 'ABCDAEFGHIJ';
# print(a.isalpha())
#
# name='tom say :i have one tesla,my name is tom'
# print(name.replace('tom','marry'))
# ret9 = 'title,Tilte,atre,'.split('t')
# print(ret9)
# a = 'ABCDAEFGHIJ';
# print(a.startswith("B",1,3))
# print(a.endswith('HI',4,10))
# a = 'ABCDAEFGHIAJ';
# ret3 = a.count("A")
# print(ret3)
# a = 'ABCDEFGHIJK'
# print(a[7])
# print(a[2:5])
# print(a[0:])
# print(a[0:-1])
# print(a[0:5:2])
#
#
# print('喜欢' in 'dkfljadklf喜欢hfjdkas')
# print('a' in 'bcvd')
# name="1255553"
# def func_name1(name):
#      print("hello world",name)
#
# func_name1(name)

# def fun_name(a,b):
#     c=a*b
#     print(c)
# x,y=5,5
# # fun_name(x,y)
# # fun_name(a=2,b=3)
# fun_name(a=2,b=5,c=6)
# def with_return(a,b):
#      return(a * b)
#      return(a + b)
# def without_return(a,b):
#      print(a*b)
#      print(a+b)

 # with_return(2,3)
# without_return(2,3)
# x=with_return(2,3)
# print(x)

# y= without_return(2,3)
# print(y)
# name,age = 'alex',18
# print(name,age)
# def func_name0():
#     name = 'oldboy'
#     age = 100
#     print(name,age)
#     print(age+1)
# func_name0()
# print(name,age)
# name,age = 'alex',18
# print(name,age)
# def func_name0():
# 	 # global name;
# 	# global age;
#     name = 'oldboy'
#     age = 100
#     print(name,age)
#     print(age+1)
# func_name0()
# print(name,age)
#1．写一个函数，接收参数n,输出n个hello word
# def fun_name(name):
#     a="hello word"
#     print(a*name)
# fun_name(5)
#2. 定义一个函数，接收三个参数num1,num2，以及符号"+","-","X","/","%",函数的内容是对符号进行判断之后，再进行计算，并且把得到的结果返回
# def fun_name(num1,num2,*args):
#     return(num1+num2)
# c=fun_name(5,2)
# print(c)
#3. 定义一个函数，接收两个参数num1,num2,函数的内容是计算两个数字的和，如果num1>num2就把两个数字的和返回，反之就不做任何处理。
# def fun_name(num1,num2,*args):
#     if num1>num2:
#         return(num1+num2)
# c=fun_name(3,2)
# print(c)

#4.定义一个函数，接收一个参数num,函数的内容为判断当前num是否为质数，如果是质数，此函数返回 true   如果不是质数此函数返回false
# def fun_name1(num):
#     if num%2==1:
#         print("true")
#     else:
#         print("false")
#
# fun_name1(9)

# s =lambda x,y:x+y
# print(s(1,9))
# d = {'a':8,'b':2,'c':3}
# print(d.items())
# res = sorted(d.items())
# res1 = sorted(d.items(),key=lambda x:x[0])
# res2 = sorted(d.items(),key=lambda x:x[1],reverse=True)
# print(res)
# print(res1)
# print(res2)
# print('here')
# print(sorted(d.items()))
# for k,v in res2:
#     print(k,v)
# print('here')
# tul=(1,2,3,4,5)
# print(tul[::-1])
# for i in tul:
#     print(i)
#
# print(tul.index(3))
# li=['tom',123,'Ture',(1,2,3,'wusir'),[1,2,3,'张三',],{'name':'tom'}]
# del li[1:4]
# print(li)
# a = [2,1,3,4,5]
#
# print(len(a))
# str="ABCDEFG"
#
#
# for i in range(len(str)-1,-1,-1):
#     print(str[i])
# s =lambda x:x*10
# print(s(2))
# d = {'a':8,'b':2,'c':3}
# print(d.items())
# res = sorted(d.items())
# res1 = sorted(d.items(),key=lambda x:x[0],reverse=True)
# res2 = sorted(d.items(),key=lambda x:x[1],reverse=True)
# print(res)
# print(res1)
# print(max(111,12))
# print(res2)
# li=[1,2,3,4,5,5,5];
# set1=set(li);
# print(set1)
# dic={
#     "name":"张三",
#     "age":23
# }
# for i in dic:
# 	  print(i,dic[i])
# class Money:
#     pass
# one = Money()
# print(type(Money))
# print(type(one))
# print(Money.__name__)  # 访问类的名称
# print(one.__class__)  # 访问实例对应的类
# class person:
#     def shilifangfa(self):
#         print('实例方法', self)
#
#     @classmethod
#     def leifangfa(ccc):
#         print('类方法', ccc)
#
#     @staticmethod
#     def jingtaifanggfa():
#         print('静态方法')
# p = person()
# p.shilifangfa()
# print(p)
# # person.shilifangfa()#TypeError: shilifangfa() missing 1 required positional argument: 'self'
# person.leifangfa()
# person.jingtaifanggfa()
# print(person.__dict__)
# print(p.__dict__)
# class Person:
#     @classmethod  # 类方法装饰器
#     def leifangfa(cls, a):  # 第一个参数默认为类
#         print('类方法', cls, a)
# Person.leifangfa(123)  # 通过类来调用
# p = Person()
# p.leifangfa(666)  # 通过实例来调用
# func = Person.leifangfa  # 通过定义函数的形式来调用
# func(111)
# class A(Person):
#     pass
# A.leifangfa(2)  # 通过衍生类来调用


# class Person:
#     @staticmethod  # 静态方法装饰器
#     def jingtai(c,a):
#         print('静态方法')
# Person.jingtai(2)  # 通过类来调用
# p = Person()
# p.jingtai(3)  # 通过实例来调用
# func = Person.jingtai  # 通过定义函数的形式来调用
# func(4)


# class Person:
#     age = 5
#     def shilifangfa(self):
#         print('实例方法', self)
#         print(self.age)
#         print(self.num)
#     @classmethod
#     def leifangfa(cls):
#         print('类方法', cls)
#         print(cls.age)
#         print(cls.num)
#     @staticmethod
#     def jingtaifanggfa():
#          print('静态方法')
#          print(Person.age)  # 访问类属性
#
#          print(Person.num)  # 访问类属性
# p = Person()
# p.num = 10
# p.shilifangfa()  # 实例方法既能访问实例属性，又能访问类属性
# # 类方法不能访问实例属性，但能访问类属性
# Person.jingtaifanggfa()

# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# # class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0    # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print (self.__secretCount)
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print (counter.publicCount)
# print (counter.__secretCount)  # 报错，实例不能访问私有变量
# print(counter.__secretCount)  # 报错，实例不能访问私有变量
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# # print(counter.__secretCount)  # 报错，实例不能访问私有变量
# print(JustCounter.count)

# class person:
#       def __init__(self,n,a):
#           self.name=n
#           self.age=a
#       def __str__(self):#信息格式化,用字符串描述实例,面向用户，通过print或str触发
#           return '姓名：{},年龄：{}'.format(self.name,self.age)
# p=person('sz',18)
# print(p.name)
# print(p,type(p))#方法里的返回值#没有__str__方法时<__main__.person object at 0x04C86070>

# class person:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, age):
#         print('姓名：{}，年龄：{}'.format(self.name, age))
#
#
# p = person('zyl')
# p(28)  # 使实例能被调用,传入参数
# p(23)
# p(14)

# class person:
#     def __init__(self):
#         self.cache = {}  # 增加一个字典属性
#
#     def __setitem__(self, key, value):  # 设置/增添键值
#         print('setitem', key, value)
#         self.cache[key] = value
#
#     def __getitem__(self, item):  # 获取键值
#         # print('getitem',item)
#         return self.cache[item]
#
#
#     def __delitem__(self, key):  # 删除操作
#         # print('setitem',key)
#         del self.cache[key]
#
#
# p = person()
# p['name'] = 'sz'  # setitem
# print(p['name'])  # getitem
# del p['name']
# print(p.cache)  # 查询字典
# class person:
#   def __init__(self,age,height):
#       self.age=age
#       self.height=height
#   def __eq__(self, other):#实现相等操作
#       print(other)
#       return self.age==other.age#返回操作后的值
#   def __ne__(self, other):#不相等
#       print('xxx')
#       return self.age!=other.age#返回操作后的值
#   def __gt__(self, other):#大于
#       return self.age>other.age#返回操作后的值
#   def __ge__(self, other):#大于等于
#       return self.age>=other.age#返回操作后的值
#   def __lt__(self, other):#小于
#       return self.age<other.age#返回操作后的值
#   def __le__(self, other):#小于等于
#       return self.age<=other.age#返回操作后的值
#
# p1=person(18,180)
# p2=person(19,190)
# print(p1==p2)
# print(p1!=p2)
# print(p1<p2)

# class Person(object):
#     def __init__(self):
#         self.__age = 18
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, value):
#         self.__age = value
#
#     # property(fget=None, fset=None, fdel=None, doc=None)
#     age = property(get_age, set_age)
#
#
# p = Person()
# print(p.age)
# p.age = 98
# print(p.age)
# print(p.__dict__)
#
#
# class Person2(object):
#     def __init__(self):
#         self.__age = 18
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         self.__age = value
#
#
# p2 = Person2()
# print(p2.age)
# p2.age = 98
# print(p2.age)
# print(p2.__dict__)
#
# class test1(object):
#     a = 10
#     b = 20
#     def get(self):
#         print('取幂：',self.a.__pow__(self.b))
#         print('求余数：',self.b.__mod__(self.a))
#         print('乘：',self.b.__mul__(self.a))
#         print('减：',self.b.__sub__(self.a))
#         print('加：',self.b.__add__(self.a))
#         print('输出:',self.b.__repr__())
#
# d = test1()
# d.get()

# class Animal():
#     def __init__(self, name):
#         self.name = name
#     def shengming(self):
#         print('dongwu11')
# class Dog(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)  # 调用父类的一个方法，从父类获得继承
#         self.color = color  # 在子类中添加新的内容
# def shengming(self):
#     print('gou1111')
#
#
# def kanjia(self):
#     print('kanjia111')
# a1 = Animal('a1')
# a2 = Dog('a2', 1)
# print(a1.shengming(), a2.shengming())


# import inspect
# class animal:
#     pass
# class person(animal):
#     pass
# #inspect.getmro(person)  # 查看类资源的访问循序
# print(person.__mro__)
# print(person.mro())

#
# class D:
#     pass
# class B(D):
#     pass
# class C(D):
#     pass
# class A(C, B):
#     pass
# print(A.mro())


# class D(object):
#     def __init__(self):
#         print("enter----D")
#         print("leave----D")
# class B(D):
#     def __init__(self):
#         print("enter----B")
#         D.__init__(self)  # 调用父类的方法
#         print("leave----B")
# class C(D):
#     def __init__(self):
#         print("enter----C")
#         super().__init__()
#         print("leave----C")
# class A(C, B):
#     def __init__(self):
#         print("enter----A")
#         B.__init__(self)
#         C.__init__(self)
#         print("leave----A")
# a=A()
# a.run();


class D:
    def __init__(self):
        print("enter----D")
        super().__init__()
        print("leave----D")
class B(D):
    def __init__(self):
        print("enter----B")
        super().__init__()
        print("leave----B")
    def __init__(self):
        print("enter----C")
        super().__init__()
class C(D):
        print("leave----C")
class A(C, B):
    def __init__(self):
        print("enter----A")
        # super沿着mro链条，找到下一级节点，去调用对应的方法
        # super(__class__, <first argument>)沿着参数二的mro链条，找参数一的下一个节点
        # 使用参数二进行调用
        super(A, self).__init__()
        # super().__init__()
        print("leave----A")
a=A()
print(A.__mro__)
