# 输出100以内的素数
# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# 输出斐波那契数列中的前 20 个数
# a, b = 0, 1
# for _ in range(20):
#     print(a)
#     a, b = b, a + b

# 找出100到999范围内的水仙花数
# for num in range(100, 1000):
#     low = num % 10
#     middle = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + middle ** 3 + high ** 3:
#         print(num)

# 百钱百鸡问题
# for x in range(0, 21):
#     for y in range(0, 34):
#         z = 100 - x - y
#         if z % 3 == 0 and x * 5 + y * 3 + z // 3 == 100:
#             print(f"x = {x}, y = {y}, z = {z}")

# 计算CRAPS赌博游戏的胜率
# from random import randint

# total = 100000  # 总轮数
# count = total
# win = 0

# while count > 0:
#     dice1 = randint(1, 6)
#     dice2 = randint(1, 6)
#     first_sum = dice1 + dice2
#     if first_sum == 7 or first_sum == 11:
#         win += 1
#     elif first_sum == 2 or first_sum == 3 or first_sum == 12:
#         win += 0
#     else:
#         needs_go_on = True
#         while needs_go_on:
#             dice1 = randint(1, 6)
#             dice2 = randint(1, 6)
#             sum = dice1 + dice2
#             if sum == 7:
#                 win += 0
#                 needs_go_on = False
#             elif sum == first_sum:
#                 win += 1
#                 needs_go_on = False
#     count -= 1

# print(f"win = {win}")
# print('在', total, '轮模拟中，玩家胜出概率为', win / total)
