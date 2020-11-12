# 列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# print(bicycles[0])
# print(bicycles[-1])

# 修改列表元素

# bicycles[0] = 'honda'
# print(bicycles)

# 列表末尾添加元素

# bicycles.append('fenghuang')
# print(bicycles)

# 在列表的任意位置插入元素

# bicycles.insert(0, 'hafou')
# print(bicycles)

# 删除元素

# del bicycles[0]
# print(bicycles)

# 使用pop() 删除

# last_bicycles = bicycles.pop()
# print(last_bicycles)
# any_bicycles = bicycles.pop(0)
# print(any_bicycles)

# 根据值删除元素(remove 只删除第一个指定的值)

# bicycles.remove('redline')
# print(bicycles)

# 排序

# bicycles.sort() # 永久排序
# print(bicycles)

# bicycles.sort(reverse=True) # 反向排序
# print(bicycles)

# 临时排序
# print(sorted(bicycles))
# print(sorted(bicycles, reverse=True))
# print(bicycles)

# 反转
# bicycles.reverse()
# print(bicycles)

# 列表长度
print(len(bicycles))
