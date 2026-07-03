# 求一个整数的阶乘
"""
def fn1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(fn1(5))
"""
"""
# 递归的规律：中止条件、递归公式
def fn(a):
    if a == 1:
        return 1
    return fn(a - 1) * a

print(fn(5))

"""
