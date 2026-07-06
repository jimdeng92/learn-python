_str = 'abc'

__bool = True

num = 100

def add(a, b):
    return a + b

# __name__ 属性可以用来判断当前模块是被直接执行还是被导入执行
if __name__ == '__main__':
    print(add(1, 2))
