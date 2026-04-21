dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = dict(a=1, b=2, c=3)
dict3 = dict([('a', 1), ('b', 2), ('c', 3)])
print(dict1, dict2, dict3)

dict1['d'] = 4
print('a' in dict1)

del dict1['a']

print(len(dict2))


# 字典遍历
for key, value in dict2.items():
    print(key, value)

for key in dict2.keys():
    print(key, dict2[key])

for value in dict2.values():
    print(value)
