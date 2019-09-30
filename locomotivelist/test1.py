import json
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# str_dic = json.dumps(dic)  #序列化：将一个字典转换成一个字符串
# print(type(str_dic),str_dic)
# dic2 = json.loads(str_dic)
# print(type(dic2),dic2)
# list_dic = [1,['a','b','c'],3,{'k1':'v1','k2':'v2'}]
# str_dic = json.dumps(list_dic) #也可以处理嵌套的数据类型
# print(type(str_dic),str_dic) #<class 'str'> [1, ["a", "b", "c"], 3, {"k1": "v1", "k2": "v2"}]
# list_dic2 = json.loads(str_dic)
# print(type(list_dic2),list_dic2) #<class 'list'> [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]
f = open('json_file','w')
dic = {'k1':'v1','k2':'v2','k3':'v3'}
json.dump(dic,f)  #dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
f.close()
f = open('json_file')
dic2 = json.load(f)  #load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
f.close()
print(type(dic2),dic2)
