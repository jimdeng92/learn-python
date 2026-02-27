# 集合类型是一种无序集合，元素唯一，不允许重复。
# 由于底层使用了哈希存储，集合中的元素必须是hashable类型
# 集合与列表最大的区别在于集合中的元素没有顺序、所以不能够通过索引运算访问元素
# 集合的元素可以是任意不可变类型。
# 创建集合
s1 = {2, 1, 3, 4, 5}
s2 = set([2, 4, 6, 8, 10])
s3 = {num for num in range(1, 6)}


print(s3)
print(s1)
print(s2)

# 集合的无序性
for num in s1:
    print(num)

print(type(s1))  # <class 'set'>
print(type(s2))

# 成员运算
print(2 in s1)
print(2 not in s1)
print(s1 == s2)

# 二元运算
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)
print(s1 <= s2)
print(s1 >= s2)
print(s1 == s2)
print(s1 != s2)
print(s1 < s2)
print(s1 > s2)

# 集合的方法
s1.add(6)
print(s1)
# 删除元素的remove方法在元素不存在时会引发KeyError错误
s1.remove(6)
print(s1)
s1.discard(6)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)

# 不可变集合
fset1 = frozenset([1, 2, 3, 4, 5])
print(fset1)
