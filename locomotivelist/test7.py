class Person(object):
    def run(self):
        print("人都跑的能力");
class Chinese(Person):
    def run(self):
        '''
        重写了父类中的run的方法
        :return:
        '''
        super().run();
        print("中国人特有的跑的行为----");
class Japanese(Person):
    def run(self):
        super().run();
        print("日本人特有的跑的行为----");
def fun1(person):
    # print(isinstance(person,Person))
    person.run();
    # 传递的是同一个类型的对象 调用的也是同一个方法 但是体现出来的效果是多样的 ---多态性
zhangsan=Chinese();
lisi=Japanese();
fun1(zhangsan);
fun1(lisi);
# a=Person()
# a.run()
# zhangsan.run()