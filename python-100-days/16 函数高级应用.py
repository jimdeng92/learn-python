# 装饰器

import random
import time
from functools import wraps
from functools import lru_cache


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}用时{end_time - start_time}秒')
        return result
    return wrapper


@record_time
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 4)
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')

# 递归


def fac(n):
    """计算阶乘"""
    if n in (0, 1):
        return 1
    else:
        return n * fac(n - 1)


# 递归调用函数入栈
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 停止递归函数出栈
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120
print(fac(5))    # 120


@lru_cache()
def fib1(n):
    """计算斐波那契数列"""
    if n in (0, 1):
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


for i in range(1, 21):
    print(fib1(i))


start_time = time.time()
print(fib1(33))
end_time = time.time()
print(f'计算fib1(33)用时{end_time - start_time}秒')
