import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接文件路径
file_path = os.path.join(current_dir, '致橡树.txt')

with open(file_path, 'r', encoding='utf-8') as file:
    print(file.read())
    # file.close() 不需要显式调用 close() 方法，with 语句会自动处理
