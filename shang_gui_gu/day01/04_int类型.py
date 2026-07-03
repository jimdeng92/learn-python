int1 = 10
int2 = 20

print(int1)
print(int2)
print(type(int1))
print(type(int2))

# 小整数池 [-5, 256]，大整数池 [256, ...]
# 声明相同的整数，会指向同一个内存地址
int3 = 100
int4 = 100
print(id(int3))
print(id(int4))

print(type(True)) # bool
print(type(1)) # int
print(isinstance(True, bool)) # True
print(isinstance(True, int)) # True



