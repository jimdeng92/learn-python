# def greet_user(username):
#   print('hello ' + username.title() + '!')

# greet_user('jimdeng')

# 位置实参
# def describe_pet(animal_type, pet_name):
#   print('\nI have a ' + animal_type + '.')
#   print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

# describe_pet('hamster', 'harry')

# 关键字实参
# def describe_pet(animal_type, pet_name):
#   print('\nI have a ' + animal_type + '.')
#   print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

# describe_pet(pet_name='harry', animal_type='hamster')

# 提供默认值
# 形参位置不可更改
# def describe_pet(pet_name, animal_type='dog'):
#   print('\nI have a ' + animal_type + '.')
#   print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

# describe_pet(pet_name='harry')

# 函数返回值
# def get_formatted_name(first_name, last_name):
#   full_name = first_name + ' ' + last_name
#   return full_name.title()

# musician = get_formatted_name('jim', 'deng')
# print(musician)

# 函数和 while
# def get_formatted_name(first_name, last_name):
#   print((first_name + ' ' + last_name).title())

# while True:
#   print('please input you name')
#   first_name = input('input your first_name: ')
#   if first_name == 'q':
#     break
#   last_name = input('input you last_name: ')
#   if last_name == 'q':
#     break
#   get_formatted_name(first_name, last_name)


# 接收任意数量的实参
# def make_pizza(*toppings):
#   print(toppings) # 元祖

# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
  profile = {}
  profile['first_name'] = first
  profile['last_name'] = last
  for key, value in user_info.items():
    profile[key] = value
  return profile

user_profile = build_profile('jim', 'deng', location='shenzhen', age='22')
print(user_profile)


# python 模块
# 直接使用文件名导入：import pizza
# 使用模块的方法：pizza.make_pizza()
# 导入特定的函数：from module_name import function_name （从某个模块导入某个函数）
# 导入多个函数：from module_name import function_0, function_1, function_2
# 为模块函数指定别名：from module_name import make_pizza as mp
# 为模块指定别名：import module_name as mn
# 导入模块所有函数：from module_name import * （慎用）
