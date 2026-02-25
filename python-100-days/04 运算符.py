"""
Python 中的运算符有 +、-、 *、 /、身份运算符（is、is not）、成员运算符（in、not in）、逻辑运算符（not、and、or）等等。
其中，3.8版本添加了海象运算符（:=），此操作符与赋值操作符（=）效果类似，但会将右边运算的结果当作返回值，因此在 print() 中不会报错。
"""

a = 0.1
b = 0.2
print(a + b)

# c = float(input('请输入摄氏度：'))
# f = c * 1.8 + 32
# print(f)

import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print(f'{perimeter = :.2f}, {area = :.2f}')