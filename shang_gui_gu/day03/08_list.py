"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list1[2]) # 3
print(list1[1:3]) # [2, 3]
print(list1[:3]) # [1, 2, 3]
print(list1[3:]) # [4, 5, 6, 7, 8, 9, 10]
print(list1[::2]) # [1, 3, 5, 7, 9]
print(list1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

list1.append(100)
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]

list1.insert(1, 100)
print(list1) # [1, 100, 2, 3, 4, 5, 6, 7, 8, 9, 10]


list1[2] = 60
print(list1) # [1, 2, 60, 4, 5, 6, 7, 8, 9, 10]

list1[2:4] = [60, 70]
print(list1) # [1, 2, 60, 70, 5, 6, 7, 8, 9, 10]

print(len(list1)) # 10

print(min(list1)) # 1

print(max(list1)) # 10

print(sum(list1)) # 55


print(10 in list1) # True
"""

"""
# 列表遍历方式
list2 = ['a', 'b', 'c', 'd']

for i in list2:
    print(i)

for i in range(len(list2)):
    print(list2[i])

for i, value in enumerate(list2):
    print(i, value)

"""
"""
# 列表推导式
list2 = ['a', 'b', 'c', 'd']

list3 = [item for item in list2 if item != 'd']
print(list3) # ['a', 'b', 'c']
"""
