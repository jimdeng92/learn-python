class Person:

    # 类属性
    home = 'earth'

    def __init__(self,name,age):
        # 实例属性
        self.name=name
        self.age=age

    # 实例方法
    def eat(self):
        print(self.name,'eat')

    # 类方法
    @classmethod
    def get_home(cls):
        print(cls.home)


    # 静态方法
    @staticmethod
    def print_any():
        print('abcdefg')


Person.get_home()
Person.print_any()
