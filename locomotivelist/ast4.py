class Hero():
    def __init__(self,name):
        self.__name = name
        self.__power = 100
    def go(self):
        if self.__power<=0:
            print("不能行走,此英雄已死亡")
        else:
            print("英雄前进")
    def eat(self,n):
        self.__power += n
        if self.__power>100:
            self.__power = 100
        print("当前体力值：",self.__power)
    def hurt(self):
        self.__power -= 10
        if self.__power<=0:
            self.__power = 0
            print("此英雄死亡")
        print("当前体力值：",self.__power)
h = Hero("阿大撒")
h.go()
for i in range(10):
    h.hurt()
h.eat(120)
