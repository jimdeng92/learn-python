def add(num1, num2):
    # if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
    #     return num1 + num2
    # else:
    #     raise TypeError('请传入数字')

    assert isinstance(num1, (int, float)) and isinstance(num2, (int, float)), '请传入数字'
    return num1 + num2

print(add(1, 2.2))

try:
    res = add('1', 2.2)
    print(res)
except TypeError as e:
    print(e)
except AssertionError as e:
    print(e)


