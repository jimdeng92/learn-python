"""
元组（Tuple）是 Python 中的一种数据结构，用于存储多个项目。元组用括号 () 表示，项目之间用逗号分隔。
元组的特点是不可变，即一旦创建，就不能修改其内容。
元组的优点是它们是不可变的，因此可以作为字典的键，而列表则不能。
"""

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

print(tup1)
print(tup2)
print(tup1 + tup2)
print(tup1 * 3)
tup1 = tup1 + (4,)
print(tup1)

# 元组遍历
for i in tup1:
    print(i)

for i in range(len(tup1)):
    print(tup1[i])

for i, item in enumerate(tup1):
    print(i, item)

