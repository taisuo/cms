import xml.sax
str='''
  <root class='1班'>
        <student id="001" score="300">张三</student>
        <student id="002" score="200">李四</student>
        <student id="003" score="100">王五</student>  
   </root>
'''
class XmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.className=""
        self.studentList=[]
        self.tempDic={}
        self.currentTag=""
#解析xml字符串
    def startElement(self,name,attr):
        self.currentTag=name
        # print("开始--", name, attr.__dict__)
        if name=="root":
             self.className=attr["class"]
             # print("开始--", name,self.rootId)
        if name=="student":
            self.tempDic["id"]=attr["id"]
            self.tempDic["score"] = attr["score"]
             # self.imgList.append(attr["src"])
    def endElement(self, name):
        if self.currentTag=="student":
            self.studentList.append(self.tempDic)
    def characters(self,content):
        # print("获取标签内容",self.currentTag,content)
        if self.currentTag=="student":
            content=content.strip()
            if len(content)>0:
                self.tempDic["name"]=content

xmlHandler=XmlHandler()
xml.sax.parseString(str,xmlHandler)
print(xmlHandler.className)
print(xmlHandler.studentList)