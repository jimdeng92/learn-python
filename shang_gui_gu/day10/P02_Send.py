# 通过生成器的send方法修改yield的返回值

def gen():
    task_id = 0
    int_value = 0
    char_value = 'A'
    while True:
        match task_id:
            case 0:
                task_id = yield int_value
                int_value += 1
            case 1:
                task_id = yield char_value
                char_value = chr(ord(char_value) + 1)
            case _:
                task_id = yield

g = gen()
print(type(g)) # <class 'generator'>
print(next(g)) # 返回int_value的值 --- 0
print(g.send(1)) # 修改yield int_value 的返回值为1，也就是赋值 task_id 为1并且再次隐式调用next(g)方法---返回A

