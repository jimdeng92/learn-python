# 面向对象编程的特点：动态、继承、多态
# 所谓动态就是：运行时可以添加、删除、修改属性和方法
# 继承是子类可以继承父类的属性和方法
# 多态是同一个方法名，不同的对象有不同的表现

# 可见性和属性装饰器
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise ValueError("age cannot be less than 0")
#         self.__age = age

#     def __str__(self):
#         return "Person(name={}, age={})".format(self.name, self.__age)


# p = Person("Alice", 18)
# print(p)
# print(p.age)
# p.age = 19
# print(p.age)


# # 动态属性
# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# stu = Student('王大锤', 20)
# stu.sex = '男'  # 给学生对象动态添加sex属性


# 继承和多态
class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生"""

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')


stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')
