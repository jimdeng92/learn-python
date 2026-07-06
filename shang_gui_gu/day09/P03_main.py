"""
导入同一个变量时，后导入的会覆盖先导入的变量
使用星号导入则只导入不以下划线开头的变量
"""
from P01_my_add import *
from P02_my_multi import num, multi
import sys

"""
python 查找模块目录的顺序：
[
    'D:\\MySpace\\learn-python\\shang_gui_gu\\day09', 
    'D:\\MySpace\\learn-python', 
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python314\\python314.zip', 
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python314\\DLLs', 
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python314\\Lib', 
    'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python314', 
    'D:\\MySpace\\learn-python\\.venv', 
    'D:\\MySpace\\learn-python\\.venv\\Lib\\site-packages'
]
"""
print(sys.path)

print(num)
# print(_str)
# print(__bool)
print(add(1, 2))
print(multi(2, 3))




