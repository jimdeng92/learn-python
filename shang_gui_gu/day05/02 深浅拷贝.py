"""
# 浅拷贝
list1 = [1, 2, 3, [4, 5, 6]]
print(list1)
copy_list1 = list1.copy()
copy_list1[3].append(7)
print(list1, copy_list1)
"""

# 深拷贝
import copy
list1 = [1, 2, 3, [4, 5, 6]]
print(list1)
copy_list1 = copy.deepcopy(list1)
copy_list1[3].append(7)
print(list1, copy_list1)
