def dog(name: str, age: int) -> tuple:
    return name, age


print(dog('WangCai', 2))

# 错误的类型不会报错
print(dog(123, 666))
