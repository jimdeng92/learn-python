
"""
# 必须参数
def print_info(name):
    print(name)

print_info("张三")

# 关键字参数
def print_info(name, age):
    print(name, age)

print_info(name="张三", age=18)

# 默认参数
def print_info(name, age=18):
    print(name, age)

print_info("张三")

# 不定长参数
def print_info(*args):
    print(args)

print_info("张三", 18, "男") # ("张三", 18, "男")
"""

"""
# 关键字不定长参数
def print_info(**kwargs):
    print(kwargs)

print_info(name="张三", age=18) # {'name': '张三', 'age': 18}

# 解包传参
def print_info(name, age):
    print(name, age)
print_info(*("张三", 18))


def print_info(name, age):
    print(name, age)

print_info(**{"name": "张三", "age": 18})
 
# 强制使用位置参数或关键字参数，/前的参数必须使用位置传参，*后的参数必须使用关键字传参
def print_info(name, age, /):
    print(name, age)

print_info(name="张三", age=18) # TypeError: print_info() got some positional-only arguments passed as keyword arguments: 'name, age'
"""

