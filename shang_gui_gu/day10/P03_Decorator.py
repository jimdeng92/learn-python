"""
装饰器是一种设计模式
它允许在不修改函数代码的前提下，动态地增加函数的功能。
装饰器本质上是一个返回函数的高阶函数，它可以在被装饰的函数执行前后添加额外的操作。
"""
from math import sqrt

# 装饰器函数
def func(x):
    return sqrt(x)

def decorator(f):
    def wrapper(x):
        x = abs(x)
        return f(x)
    return wrapper

# 使用装饰器
print(decorator(func)(-4))

# 装饰器语法糖
@decorator
def func2(x):
    return sqrt(x)

print(func2(-4))
