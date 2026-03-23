import orjson
import os


# my_dict = {
#     'name': '骆昊',
#     'age': 40,
#     'friends': ['王大锤', '白元芳'],
#     'cars': [
#         {'brand': 'BMW', 'max_speed': 240},
#         {'brand': 'Audi', 'max_speed': 280},
#         {'brand': 'Benz', 'max_speed': 280}
#     ]
# }

# # 序列化
# print(orjson.dumps(my_dict))


# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接文件路径
file_path = os.path.join(current_dir, 'data.json')

with open(file_path, 'r') as file:
    my_dict = orjson.loads(file.read())
    print(my_dict)
