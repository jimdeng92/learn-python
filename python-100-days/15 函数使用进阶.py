# Lambda函数
# old_nums = [35, 12, 8, 99, 60, 52]
# new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
# print(new_nums)


# 用一行代码实现计算阶乘的函数
# factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
# print(factorial(5))

# 用一行代码实现判断素数的函数
# is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
# print(is_prime(17))

# 偏函数
import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int('1001'))    # 1001

print(int2('1001'))   # 9
print(int8('1001'))   # 513
print(int16('1001'))  # 4097
