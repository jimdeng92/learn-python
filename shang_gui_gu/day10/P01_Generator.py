# 生成器

""" 生成器形式一
from collections.abc import Iterable, Iterator

gen = (i for i in range(100))

print(gen)

print(isinstance(gen, Iterable))
print(isinstance(gen, Iterator))
"""

""" 生成器形式二
# 斐波那契数列
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

f = fibonacci()
print(type(f)) # <class 'generator'>

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
"""

# 拿到生成器函数的返回值
def fibonacci():
    a, b, count = 0, 1, 0
    while count < 10:
        yield b
        a, b, count = b, a+b, count+1
    return 'abcedfgfdecba'

f = fibonacci()
print(type(f))

try:
    while True:
        print(next(f))
except StopIteration as e:
    print(e) # abcedfgfdecba
