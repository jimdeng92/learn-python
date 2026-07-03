"""
匿名函数：lambda函数
# 计算两个数之间的加、减、乘、除
"""

def calc(num1, num2, fn):
    return fn(num1, num2)

def plus(num1, num2):
    return calc(num1, num2, lambda x, y: x + y)

def minus(num1, num2):
    return calc(num1, num2, lambda x, y: x - y)

def multiply(num1, num2):
    return calc(num1, num2, lambda x, y: x * y)

def divide(num1, num2):
    return calc(num1, num2, lambda x, y: x / y)

def my_map(fn, lst):
    return [fn(x) for x in lst]

print(my_map(lambda x: x ** 2, [1, 2, 3, 4, 5]))

