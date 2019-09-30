# class Student:
#     count=0
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         Student.count+=1
# ming=Student("小明",25,"male")
# hong=Student("小红",25,"female")
# lan=Student("小兰",25,"female")
# print(Student.count)


class Vehicle():
    def __init__(self,speed,size):
        self.__speed = speed      #初始化
        self.size = size
    def move(self,s):
        print("移动了%s"%s)
    def setSpeed(self,speed):
        if str(speed).isdigit():
            self.__speed = speed       #赋值
        else:
            print("请输入正确速度")
    def speedUp(self):
        self.__speed += 10
        print("当前速度",self.__speed)
    def speed_Down(self):
        self.__speed -= 10
        print("当前速度",self.__speed)
def test():
    v = Vehicle(30,15)
    v.move(50)
    v.setSpeed(40)
    v.speedUp()
    v.speedUp()
    v.speed_Down()
if __name__ == "__main__":
    test()
