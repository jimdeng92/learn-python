# 函数是对功能相对独立且会重复使用的代码的封装
def my_function():
    print("Hello, World!")


my_function()

m = int(input("请输入一个数字(m)："))
n = int(input("请输入一个数字(n)："))

# 阶乘函数

# 计算阶乘


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(m))
print(factorial(n))

# 函数参数


def add1(a, b):
    return a + b


print(add1(3, 5))
print(add1(a=3, b=5))

# 函数参数默认值


def add2(a, b=5):
    return a + b


print(add2(3))

# 可变参数


def add3(*args):
    sum = 0
    for arg in args:
        if type(arg) in (int, float):
            sum += arg
    return sum


print(add3(1, 2, 3, 4, 5))

# python 标准库中的内置函数
print(abs(-5))
print(round(3.7))
print(max(1, 2, 3, 4, 5))
print(min(1, 2, 3, 4, 5))
print(sum(1, 2, 3, 4, 5))
print(len("Hello, World!"))
print(str("Hello, World!"))
print(type("Hello, World!"))
print(list("Hello, World!"))
print(dict(a=1, b=2, c=3))
print(sorted([5, 2, 3, 1, 4]))
print(reversed([5, 2, 3, 1, 4]))
print(type([5, 2, 3, 1, 4]))
print(type("Hello, World!"))
print(type({}))
print(type([]))
print(type(()))
print(type({1: "a", 2: "b", 3: "c"}))
print(type(range(1, 10)))
print(type(None))
print(type(True))
