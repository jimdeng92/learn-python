try:
    num = 10 / 0
    print(num)
except ZeroDivisionError as e:
    print('除数不能为零', e) # division by zero
except (NameError, TypeError) as e:
    print(e)
except:
    print('未知错误')
finally:
    print('执行完毕')
