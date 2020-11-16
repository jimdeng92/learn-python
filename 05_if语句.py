# if 语句

# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#   if car == 'bmw':
#     print(car.upper())
#   else:
#     print(car.title())


# 不相等
# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#   print('Hold the anchovies!')


# and 和 or
# age_0 = 22
# age_1 = 18

# if age_0 >= 21 and age_1 >= 21:
#   print('all is good')
# elif age_0 >=21 or age_1 >=21:
#   print('is ok yet')
# else:
#   print('is bad')


# 检查特定值是否在列表中

# requested_toppings = ['mushrooms', 'onions', 'pineapple']

# print('mushrooms' in requested_toppings)

# print('onions' not in requested_toppings)

# 练习

# alien_color = ['green', 'yellow', 'red']

# del alien_color[1]

# if 'green' not in alien_color:
#   print('you get 5 point')
# elif 'yellow' not in alien_color:
#   print('you get 10 point')
# elif 'red' not in alien_color:
#   print('you get 15 point')

# 确定列表不是空的

requested_toppings = []

if requested_toppings:
  for requested_topping in requested_toppings:
    print('Adding' + requested_topping + '.')
  print('\nFinished making your pizza!')
else:
  print('Are you sure you want a plain pizza?')
