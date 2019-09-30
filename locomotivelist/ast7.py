import os
import stat
import shutil


# filePath:文件夹路
# def delete_file(filePath):
#     if os.path.exists(filePath):
#         for fileList in os.walk(filePath):
#             for name in fileList[2]:
#                 os.chmod(os.path.join(fileList[0], name), stat.S_IWRITE)
#                 os.remove(os.path.join(fileList[0], name))
#         shutil.rmtree(filePath)
#         return "delete ok"
#     else:
#         return "no filepath"
#
#
# print
# os.path.exists("G:\\pythonwork\\server\\locomotivelist\\aaa")
# print
# delete_file("G:\\pythonwork\\server\\locomotivelist\\aaa")
# from datetime import datetime,timedelta
# time1 = datetime.now()
# time2=time1.timestamp()
# print(time2)
# str="2019-8-8 10:10:10"
# cday = datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
# print(cday)
# time3=cday.timestamp()
# print(time3)
# time4=time2-time3
# print(time4)
# import os
# def delDir(dir):
#     # 判断传递过来的dir是否存在
#     if not os.path.exists(dir):
#         print("当前目录不存在")
#         return
#     if os.path.exists(dir):
#         # 判断当前dir是文件还是文件夹
#         if os.path.isfile(dir):
#             # 当前是文件
#             print("文件",dir)
#             os.remove(dir)
#             return
#         # 当前是文件夹
#         # 判断当前文件夹是否为空
#         dirlist=os.listdir(dir)
#         if len(dirlist)==0:
#             print("文件夹是空",dir)
#             # 删除空的文件夹
#             os.rmdir(dir)
#             return
#         # 当前文件夹非空
#         print("文件夹非空")
#         for item in dirlist:
#             # 查看当前item是文件还是文件夹
#             itemPath = os.path.join(dir, item)
#             # itemPath = item
#             if os.path.isfile(itemPath):
#                 # 当前是文件 相对于当前文件所在的目录去查找item
#                 # 查找到item的绝对路径
#                 print("其中包含文件",itemPath)
#                 os.remove(itemPath)
#             else:
#                 #查找到了是文件夹
#                 print("其中包含文件夹", itemPath)
#                 delDir(itemPath)
#         else:
#             os.rmdir(dir)
# path=os.path.join(os.getcwd(),"aaa")
# print(path)
# delDir(path)
# import xml.sax
#
#
# class MovieHandler(xml.sax.ContentHandler):
#     def __init__(self):
#         self.CurrentData = ""
#         self.type = ""
#         self.format = ""
#         self.year = ""
#         self.rating = ""
#         self.stars = ""
#         self.description = ""
#
#     # 元素开始事件处理
#     def startElement(self, tag, attributes):
#         self.CurrentData = tag
#         if tag == "movie":
#             print
#             "*****Movie*****"
#             title = attributes["title"]
#             print
#             "Title:", title
#
#     # 元素结束事件处理
#     def endElement(self, tag):
#         if self.CurrentData == "type":
#             print
#             "Type:", self.type
#         elif self.CurrentData == "format":
#             print
#             "Format:", self.format
#         elif self.CurrentData == "year":
#             print
#             "Year:", self.year
#         elif self.CurrentData == "rating":
#             print
#             "Rating:", self.rating
#         elif self.CurrentData == "stars":
#             print
#             "Stars:", self.stars
#         elif self.CurrentData == "description":
#             print
#             "Description:", self.description
#         self.CurrentData = ""
#
#     # 内容事件处理
#     def characters(self, content):
#         if self.CurrentData == "type":
#             self.type = content
#         elif self.CurrentData == "format":
#             self.format = content
#         elif self.CurrentData == "year":
#             self.year = content
#         elif self.CurrentData == "rating":
#             self.rating = content
#         elif self.CurrentData == "stars":
#             self.stars = content
#         elif self.CurrentData == "description":
#             self.description = content
#
#
# if (__name__ == "__main__"):
#     # 创建一个 XMLReader
#     parser = xml.sax.make_parser()
#     # turn off namepsaces
#     parser.setFeature(xml.sax.handler.feature_namespaces, 0)
#
#     # 重写 ContextHandler
#     Handler = MovieHandler()
#     parser.parse("sss.xml")
# parser.setContentHandler(Handler)

# from datetime import datetime
# dt = datetime(2015, 4, 19, 12, 10, 10) # 用指定日期时间创建datetime
# dt.timestamp() # 把datetime转换为timestamp
# ts=dt.timestamp() # 把datetime转换为timestamp
# print(ts)
#
# time1 = datetime.now()
# time2=time1.timestamp()
# print(time2)
# print(time1)
from xml.dom.minidom import parse

# minidom解析器打开xml文档并将其解析为内存中的一棵树
DOMTree = parse(r'avw')
# 获取xml文档对象，就是拿到树的根
collection = DOMTree.documentElement

if collection.hasAttribute('shelf'):
    # 判断根节点collection是否有shelf属性,有则获取并打印属性值
    print('Root element is ', collection.getAttribute('shelf'))

# 获取所有的movies节点
movies = collection.getElementsByTagName('movie')

# 遍历集合，打印每部电影的详细信息
for movie in movies:
    print("*******************movie*******************")
    my_list = []
    if movie.hasAttribute('title'):
        print('title is ', movie.getAttribute('title'))

    for node in movie.childNodes:
        my_list.append(node.nodeName)
    type = movie.getElementsByTagName('type')[0]
    print('type is ', type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print('format is ', format.childNodes[0].data)

    if 'year' in my_list:
        year = movie.getElementsByTagName('year')[0]
        print('year is ', year.childNodes[0].data)

    rating = movie.getElementsByTagName('rating')[0]
    print('rating is ', rating.firstChild.data)

    stars = movie.getElementsByTagName('stars')[0]
    print('stars is ', stars.childNodes[0].data)

    description = movie.getElementsByTagName('description')[0]
    print('description is ', description.childNodes[0].data)
