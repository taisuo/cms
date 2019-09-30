f=open('file','r',encoding='utf-8')
# print(f.readline())
print(f.read())
import os
import sys
# print(os.name)
# print(os.getcwd)
# print(os.path.abspath('.'))
# path = os.path.join('./', 'testdir')
# path = os.path.join('.','ast.py')
# print(path)
# os.mkdir(path)
# os.rmdir(path)
# os.path.split('/Users/michael/testdir/file.txt')
# print(os.path.split('/Users/michael/testdir/file.txt')[1])
# print(os.path.splitext('/Users/michael/testdir/file.txt'))
# os.rename((os.path.join('./ast1.py', 'st1st1.py')
# # for x in os.listdir('.')
#  print(os.listdir('.'))
def search_file(path, str):  # 传入当前的绝对路径以及指定字符串
    # 首先先找到当前目录下的所有文件
    for file in os.listdir(path):  # os.listdir(path) 是当前这个path路径下的所有文件的列表
        this_path = os.path.join(path, file)
        print("******"+this_path)
        if os.path.isfile(this_path):  # 判断这个路径对应的是目录还是文件，是文件就走下去
            if str in file:
                print(this_path)
        else:   # 不是就再次执行这个函数，递归下去
            search_file(this_path, str)  # 递归下去

if __name__ == "__main__":
    search_file(os.path.abspath("."), "ast")
