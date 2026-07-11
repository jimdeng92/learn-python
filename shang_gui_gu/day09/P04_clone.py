list1 = [1, 2, 3]

# 浅拷贝的几种方式
list2 = list1.copy()
list3 = list(list1)
list4 = list1[:]
print(id(list1))
print(id(list2))
print(id(list3))
print(id(list4))

# 深拷贝
import copy
list5 = [1, 2, 3, [4, 5, 6]]
list6 = copy.deepcopy(list5)
list7 = [1, 2, 3, [4, 5, 6]]
list8 = copy.copy(list7)
print(id(list5), id(list5[0]), id(list5[1]), id(list5[2]), id(list5[3]))
print(id(list6), id(list6[0]), id(list6[1]), id(list6[2]), id(list6[3]))
print(id(list7), id(list7[0]), id(list7[1]), id(list7[2]), id(list7[3]))
print(id(list8), id(list8[0]), id(list8[1]), id(list8[2]), id(list8[3]))
