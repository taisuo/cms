class Animal:
    def __init__(self, name,life_value,aggressivity):
        self.name = name
        self.life_value = life_value
        self.aggressivity = aggressivity
    def attack(self,enemy):
        enemy.life_value -= self.aggressivity
class People(Animal):
    camp='home'
    def attack(self,enemy):
        super().attack(enemy)
        print('from people')
class Dog(Animal):
    camp='wo'
    def attack(self,enemy):
        super().attack(enemy)
        # print('from dog')
p1=People('alice',100,5)
p1=People('alex',100,5)
d1=Dog('w1',100,10)
d2=Dog('w2',100,10)
d3=Dog('w3',100,10)
print(p1.life_value)
d1.attack(p1)
print(p1.life_value)

print(d1.life_value)
p1.attack(d1)
print(d1.life_value)
