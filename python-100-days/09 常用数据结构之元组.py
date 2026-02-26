# 元组是不可变类型，即元组创建后其内容不能被修改，但可以对元组进行连接、重复、成员判断等操作。
# 元组创建后其内容不能被修改，但可以对元组进行连接、重复、成员判断等操作。
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (6, 7, 8, 9, 10)
# tuple3 = tuple1 + tuple2
# print(tuple3)
# print(type(tuple3))  # <class 'tuple'>
# print(tuple3 * 2)
# print(3 in tuple3)
# print(3 not in tuple3)
# print(tuple3[0])
# print(tuple3[0:5])
# print(len(tuple3))
# print(max(tuple3))
# print(min(tuple3))
# print(tuple3.count(3))
# print(tuple3.index(3))
# print(tuple3[0:5:2])
# print(tuple3[0:5:-1])
# print(tuple3[0:5:1])
# print(('hello',))  # 一元组需要在元素后加逗号

# import timeit

# print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
# print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

infos = ('辰良', '男', 18)

print(list(infos))

frts = ['apple', 'banana', 'cherry']

print(tuple(frts))
