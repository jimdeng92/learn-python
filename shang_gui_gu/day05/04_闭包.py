"""闭包的定义：如果在一个函数内部定义了另一个函数，并且这个内部函数引用了外部函数的变量，那么这个内部函数就是闭包。"""
"""
def outer():
    a = 10
    def inner():
        print(a)

    return inner

outer()()
"""
