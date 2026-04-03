for i in range(1, 20):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i)


sum1 = 0
for i in range(1, 101):
    sum1 += i
    print(i, sum1)
    if sum1 > 100:
        break  # 跳出循环
