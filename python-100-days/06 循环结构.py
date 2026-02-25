"""
range(起始值，结束值，步进)
"""

# total = 0
#
# for i in range(1, 101):
#     total += i
#
# print(total)

# for in 循环求和
# total = 0
# for i in range(1, 101, 2):
#     total += i
# print(total)

# 使用内置sum求和
# sum 函数的参数是一个可迭代对象，如列表、元组等，而 range 是一个内置函数，返回一个可迭代对象
# total = sum(range(1, 101))
# print(total)

# while 循环求和，当 while 后面的表达式为 False 时，循环终止
# total = 0
# i = 1
# while i <= 100:
#     total += i
#     i += 1
# print(total)

# 使用 break 终止循环
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# 使用 continue 跳过当前循环，继续下一次循环
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# 嵌套循环打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {i * j}", end="\t")  # 打印一行乘法表, \t 空格
#     print()  # 换行

# 输入一个大于1的正整数判断它是不是素数
# num = int(input("请输入一个大于1的正整数："))
# if num <= 1:
#     print("请输入一个大于1的正整数")
# else:
#     start = 2
#     end = int((num ** 0.5) + 1)  # 因子都是成对出现的，只需要判断到它的平方根
#     is_prime = True
#     for i in range(start, end):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("它是一个素数")
#     else:
#         print("它不是素数")

# 输入两个正整数求它们的最大公约数
# a = int(input("请输入第一个正整数："))
# b = int(input("请输入第二个正整数："))
# if a <= 0 or b <= 0:
#     print("请输入大于0的正整数")
# else:
#     if a > b:
#         a, b = b, a  # 交换 a 和 b 的值
#     for i in range(a, 0, -1):
#         if a % i == 0 and b % i == 0:
#             print(f"{a} 和 {b} 的最大公约数是 {i}")
#             break

# 猜数字小游戏
import random

answer = random.randrange(1, 101)
count = 0
while True:
    count += 1
    guess = int(input("请输入你的猜测："))
    if guess > answer:
        print("太大了")
    elif guess < answer:
        print("太小了")
    else:
        print("恭喜你猜对了")
        break
print(f"你一共猜了 {count} 次")
