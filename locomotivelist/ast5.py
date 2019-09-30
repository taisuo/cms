class Vehicles():
    def __init__(self,brand,color):
        self.__brand = brand         #_Vehicles__brand
        self.__color = color

    def run(self):
        print("我已经开动了")
    def showInfo(self):
        print(self.__brand,self.__color)

class Car(Vehicles):
    def __init__(self,brand,color,seats):
        super().__init__(brand,color)
        self.__seats = seats
    def showCar(self):
        self.showInfo()
        print(self.__seats)
class Truck(Vehicles):
    def __init__(self,brand,color,load):
        super().__init__(brand,color)
        self.__load = load
    def showTruck(self):
        self.showInfo()
        print(self.__load)

c = Car("7Q","绿色",5)
c.run()
c.showCar()
t = Truck("五菱宏光","蓝色",6.66)
t.run()
t.showTruck()
