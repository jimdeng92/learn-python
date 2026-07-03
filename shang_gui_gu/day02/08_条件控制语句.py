from random import randint

num = randint(1, 100)

if num % 3 == 0:
    print(f"{num} 是3的倍数")
elif num % 3 == 1:
    print(f"{num} 除以3余1")
else:
    print(f"{num} 除以3余2")

