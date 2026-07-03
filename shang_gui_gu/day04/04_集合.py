"""
集合（Set）是 Python 中的一种数据结构，用于存储多个项目。集合用花括号 {} 表示，项目之间用逗号分隔。
集合的特点是无序、不重复。集合中的元素必须是不可变类型。
集合常用方法：
add()：添加元素
remove()：删除元素
discard()：删除元素，如果元素不存在则不报错
pop()：随机删除元素
clear()：清空集合
update()：更新集合
intersection_update()：交集更新
union_update()：并集更新
difference_update()：差集更新
symmetric_difference_update()：对称差集更新
issubset()：判断子集
issuperset()：判断超集
isdisjoint()：判断是否无交集
copy()：复制集合
frozenset()：创建不可变集合
set()：创建集合


"""

set1 = {1, 2, 3}
set2 = {4, 5, 6}

empty_set = set()

print(set1)
print(set2)

set1.add(4)
print(set1)
set1.remove(2)
print(set1)

# 运算符求两个集合的交集、并集、差集
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
