# 面向对象
import time
from tkinter import Y


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    def watch_movie(self):
        if self.age >= 18:
            print(f'{self.name}正在观看电影')
        else:
            print(f'{self.name}正在观看动画')


s1 = Student('Tom', 12)
s1.study('Python')
s1.watch_movie()
Student.study(s1, 'Python')
Student.watch_movie(s1)


# 定义一个类描述数字时钟，提供走字和显示时间的功能
# class Clock:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second

#     def run(self):
#         self.second += 1
#         if self.second == 60:
#             self.second = 0
#             self.minute += 1
#             if self.minute == 60:
#                 self.minute = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0

#     def show(self):
#         return f'{self.hour:02}:{self.minute:02}:{self.second:02}'


# clock = Clock(23, 59, 58)
# while True:
#     print(clock.show())
#     time.sleep(1)
#     clock.run()


# 定义一个类描述平面上的点，提供计算到另一个点距离的方法
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def __str__(self):
        return f'({self.x}, {self.y})'


print(Point(1, 2).distance_to(Point(4, 6)))
