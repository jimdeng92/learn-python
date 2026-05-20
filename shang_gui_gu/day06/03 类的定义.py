class Person:
    """
    创建人的类
    """

    home = 'earth'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('eating')

    def swim(self):
        print('swimming')


lilei = Person('lilei',18)
lilei.eat()
lilei.swim()
