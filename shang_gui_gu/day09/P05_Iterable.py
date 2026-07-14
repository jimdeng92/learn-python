from collections.abc import Iterable, Iterator

list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
dict1 = {'a': 1, 'b': 2, 'c': 3}
set1 = {1, 2, 3}

for item in list1:
    print(item)
for item in tuple1:
    print(item)
for item in set1:
    print(item)
for key in dict1:
    print(key)

print(isinstance(list1, Iterable)) # True
print(isinstance(tuple1, Iterable)) # True
print(isinstance(set1, Iterable)) # True
print(isinstance(dict1, Iterable)) # True
print(isinstance(list1, Iterator)) # False
print(isinstance(tuple1, Iterator)) # False
print(isinstance(set1, Iterator)) # False
print(isinstance(dict1, Iterator)) # False

# 可迭代对象都有内置的__iter__和__next__方法，通过 iter()和next()调用

iter1 = iter(list1)
print(next(iter1)) # 1
print(next(iter1)) # 2
print(next(iter1)) # 3
# print(next(iter1)) # StopIteration


# 自定义迭代器对象
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


reverse_list = Reverse([1, 2, 3, 4, 5])
print(list(reverse_list)) # [5, 4, 3, 2, 1]
