"""
    给定一个三位的状态码，左边第一位表示大小写状态，1-大写 0 -小写
    第二位标识输入法语言，1 - 简体中文 0 - 英文
    第三位鄙视输入法模式 1 - 中文 0 - 英文
"""

from random import randint

list1 = [randint(0, 1) for _ in range(3)]

for (i, j) in enumerate(list1):
    if i == 0:
        print('大写' if j == 1 else '小写')
    elif i == 1:
        print('简体中文' if j == 1 else '英文')
    elif i == 2:
        print('中文' if j == 1 else '英文')


