class Person:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f'{self.name} is eating')

class Teacher(Person):
    pass

class Student(Person):
    pass



def eat(obj):
    obj.eat()

t1 = Teacher('za')
s2 = Student('ls')
eat(t1)
eat(s2)


# ----------------------------------------------------------------------
# 上面的 Teacher / Student 都是 pass，没有重写 eat，看不出多态的意义。
# 多态的关键：子类对同一方法给出不同实现，同一个调用接口表现出不同行为。
# ----------------------------------------------------------------------

class Person2:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')


class Teacher2(Person2):
    def eat(self):  # 重写：不同实现
        print(f'老师 {self.name} 在办公室吃饭')


class Student2(Person2):
    def eat(self):  # 重写：不同实现
        print(f'学生 {self.name} 在食堂吃饭')


def have_meal(obj):  # 同一接口，不关心 obj 的具体类型
    obj.eat()


have_meal(Teacher2('za'))   # 老师 za 在办公室吃饭
have_meal(Student2('ls'))   # 学生 ls 在食堂吃饭


# Python 的多态不依赖继承（鸭子类型）：
# 只要对象有 eat() 方法就能调用，无需是 Person2 的子类。
class Dog:
    def eat(self):
        print('狗在啃骨头')


have_meal(Dog())            # 狗在啃骨头

