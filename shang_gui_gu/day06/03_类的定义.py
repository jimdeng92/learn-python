class Person:
    """
    创建人的类
    """

    # 类属性
    home = 'earth'

    def __init__(self,name,age):
        # 实例属性
        self.name=name
        self.age=age

    def eat(self):
        print('eating')

    def swim(self):
        print('swimming')


lilei = Person('lilei',18)
lilei.eat()
lilei.swim()
