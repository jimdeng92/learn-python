# 数据类型之列表
# print(type([1, 2, 3, 4, 5, 6])) # <class 'list'>
# print(list(range(1, 7)))
# print(list('hello'))
# print([1, 2, 3, 4, 5, 6] + ['hello'])
# print([0] * 6)
# print(1 in [1, 2, 3, 4, 5, 6])
# print(100 not in [1, 2, 3, 4, 5, 6])
# print([1, 2, 3, 4, 5, 6][0])
# print([1, 2, 3, 4, 5, 6][5])
# print([1, 2, 3, 4, 5, 6][-1])
# print([1, 2, 3, 4, 5, 6][-6])
# print([1, 2, 3, 4, 5, 6][0:3])  # [1, 2, 3]
# print([1, 2, 3, 4, 5, 6][0:6])  # [1, 2, 3, 4, 5, 6]
# print([1, 2, 3, 4, 5, 6][3:6])  # [4, 5, 6]
# print([1, 2, 3, 4, 5, 6][0:6:2])  # [1, 3, 5]
# print([1, 2, 3, 4, 5, 6][::-1])  # [6, 5, 4, 3, 2, 1]
# print([1, 2, 3, 4, 5, 6][::2])  # [1, 3, 5]
# num1 = [1, 2, 3, 4, 5, 6]
# num2 = list(range(1, 7))
# print(num1 == num2)

# 将一颗色子掷 6000 次，统计每种点数出现的次数
# from random import randint

# count = 6000
# result = [0] * 6

# for _ in range(count):
#     result[randint(1, 6) - 1] += 1

# for i in range(1, 7):
#     print(f"{i} 点出现了 {result[i - 1]} 次")

# 列表元素遍历
# for i in [1, 2, 3, 4, 5, 6]:
#     print(i)

# 列表的方法
# append() 方法
# list1 = [1, 2, 3, 4, 5, 6]
# list1.append(7)
# print(list1)

# # insert() 方法
# list1.insert(0, 0)
# print(list1)

# # remove() 方法
# list1.remove(7)

# language = ['Python', 'Java', 'C++', 'JavaScript', 'Python']

# if 'Python' in language:
#     language.remove('Python')

# print(language)  # 列表有重复元素时，remove() 方法只会删除第一个匹配的元素

# del language[0]  # del 与 pop() 方法都可以删除指定索引的元素，pop() 方法会返回被删除的元素

# print(language)

# index() 方法
# list1 = [1, 2, 3, 4, 5, 6]
# print(list1.index(3))

# count() 方法
# list1 = [1, 2, 3, 4, 5, 6]
# print(list1.count(3))

# sort() 方法
# list1 = [2, 11, 3, 4, 55, 6]
# list1.sort()
# print(list1)

# reverse() 方法
# list1 = [1, 2, 3, 4, 5, 6]
# list1.reverse()
# print(list1)

# 生成式（列表生成式）
# list1 = [i for i in range(1, 7)]
# print(list1)
# list2 = [i for i in range(1, 7) if i % 2 == 0]
# print(list2)
# list3 = [i ** 2 for i in range(1, 7)]
# print(list3)


# 双色球随机选号程序
import random
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(show_header=True)

n = int(input("生成几注随机选号："))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
for col_name in ['序号', '红球', '蓝球']:
    table.add_column(col_name)

for i in range(n):
    red_balls_selected = random.sample(red_balls, 6)
    blue_ball_selected = random.choice(blue_balls)
    table.add_row(
        str(i + 1), str(' '.join(map(str, red_balls_selected))), str(blue_ball_selected))
console.print(table)
