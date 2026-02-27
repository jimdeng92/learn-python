# 设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置
import random


def generate_verification_code(length=4):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    verification_code = ''.join(random.choice(characters)
                                for i in range(length))
    return verification_code


print(generate_verification_code(6))

# 设计一个判断给定的大于1的正整数是不是质数的函数。质数是只能被1和自身整除的正整数（大于1），如果一个大于 1 的正整数N是质数，那就意味着在 2 到N−1之间都没有它的因子


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


print(is_prime(29))

# 最大公约数和最小公倍数的计算


def gcd(a, b):
    """计算最大公约数"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """计算最小公倍数"""
    return a * b // gcd(a, b)


print(gcd(24, 36))
print(lcm(24, 36))


# 双色球随机选号
def random_double_color_ball():
    red_ball = [i for i in range(1, 34)]
    blue_ball = [i for i in range(1, 17)]
    red_ball_selected = random.sample(red_ball, 6)
    blue_ball_selected = random.choice(blue_ball)
    return red_ball_selected, blue_ball_selected


print(random_double_color_ball())
