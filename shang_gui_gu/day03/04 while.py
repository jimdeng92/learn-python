"""
# 计算第十周有多少只兔子
current_num = 2
current_week = 2

while current_week <= 10:
    current_num *= 3
    print(f'第{current_week}周，有{current_num}只兔子')
    current_week += 1
"""
# 打印进度条
from time import sleep
import random

step = 0
while step < 100:
    step += 1
    print(f'\r{'=' * step} {step}%', end='')
    sleep(random.random())

