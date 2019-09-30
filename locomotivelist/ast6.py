# print('喜欢' in 'dkfljadklf喜欢hfjdkas')
# print('a' in 'bcvd')
# print('y' not in 'ofkjdslaf')
# int="123456789"
# print("1" in int)
dic=123
print(id(dic)) #看内存地址


class Money:
    pass  # 占位符


one = Money()
# 类的实例对象
print(type(Money))
print(type(one))
print(Money.__name__)  # 访问类的名称
print(one.__class__)  # 访问实例对应的类
