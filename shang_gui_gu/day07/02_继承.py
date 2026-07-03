"""单继承"""
class Person:
    # 类属性
    home="earth"
    def __init__(self,name):
        # 实例属性
        self.name=name

    def eat(self):
        print(f'{self.name} is eating')

class YellowRacer(Person):
    color="yellow"

    def __init__(self,name,age):
        super().__init__(name) # super() 相当于父类 Person
        self.age=age

class WhiteRacer(Person):
    color="white"

    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

y1 = YellowRacer('y1', 22)
print(y1.age, y1.name, y1.home, y1.color)
y1.eat()
w1 = WhiteRacer('w1', 23)
print(w1.age, w1.name, w1.home, w1.color)
