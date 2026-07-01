"""
# 私有属性或方法通过添加双下划线强制标记
# 但是还是可以通过 _[类名]__[属性/方法]访问
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def __private_method(self):
        print('private_method')


p1 = Person('zs', 22)

print(p1.name)
# print(p1.__age) # AttributeError: 'Person' object has no attribute '__age'
# print(p1._Person__age)
# print(p1.__private_method) # AttributeError: 'Person' object has no attribute '__private_method'. Did you mean: '_Person__private_method'?
"""

# 私有属性或方法装饰器
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    # 私有属性装饰器
    @property
    def age(self):
        if self.__age > 18:
            return 18
        return self.__age

    # 私有方法装饰器
    @age.setter
    def age(self,age):
        self.__age=age


p1 = Person('zs', 22)
print(p1.age)
p1.age = 25
print(p1.age)
