"""
var0 = 10

def fn1():
    # 声明var0为全局变量
    global var0
    var0 = 20
    print(var0)

fn1()
print(var0)
"""

def outer():
    var0 = 10
    def inner():
        nonlocal var0 # 声明var0为非局部变量
        var0 = 20
        print(var0)

    inner()
    print(var0)

outer()


