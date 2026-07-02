class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def add(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    else:
        raise MyException('错误')

try:
    add('1',2)
except MyException as e:
    print(e)
