"""
多层装饰器
"""
from math import sqrt

def func(x):
    return sqrt(x)

def get_abs(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

def get_integer(f):
    def inner(x):
        x = int(x)
        return f(x)
    return inner

# 错误
# print(get_abs(get_integer(func))('-4'))
print(get_integer(get_abs(func))('-4'))
