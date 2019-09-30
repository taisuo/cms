from exception1 import MyException

def judgeNum(num):
    if num<1:
        e=MyException.MyException("当前num小于1",__file__)
        raise e
    elif num>=1 and num<10:
        raise MyException.MyException("当前num大于1小于10 不满足条件",__file__)
    else:
        num+=10
        return num
def test():
    try:
        num=judgeNum(0)
        print(num)
    except MyException.MyException as e:
         print(e)
test()
# from datetime import datetime
# import os
# import sys
# class MyException(Exception):
#     def __init__(self,error,currenrFile):
#         super().__init__(error)
#         # 加入自己额外的功能  写错误日志
#         # xml1/error.log
#         # 错误信息 error
#
#         # 出错时间
#         errortime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         print(errortime)
#         # 出错所在的文件
#         file=currenrFile
#         # 出错所在的函数
#         errorFun=sys._getframe().f_back.f_code.co_name
#         # 出错de行数
#         lineNumber = sys._getframe().f_back.f_lineno
#         errorstr="出错的时间："+errortime+";出错的文件："+file+";出错的函数名："+errorFun+";出错的行数："+str(lineNumber)+";出错的信息："+error+"\n"
#
#         f=open("xml1/error.log","a+",encoding="utf8")
#         f.write(errorstr)
# MyException()