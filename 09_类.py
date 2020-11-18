# 创建 Dog 类
# class Dog():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def sit(self):
#     print(self.name.title() + ' is now sitting.')
#   def roll_over(self):
#     print(self.name.title() + ' rolled over!')

# my_dog = Dog('willie', 6)
# print(my_dog.name)
# my_dog.sit()
# my_dog.roll_over()

# your_dog = Dog('lucy', 3)

# Car 类
# class Car():
#   def __init__(self, make, model, year):
#     self.make = make
#     self.model = model
#     self.year = year
#     self.odometer_reading = 0
#   def get_descriptive_name(self):
#     long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#     return long_name.title()
#   def read_odometer(self):
#     print('This car has ' + str(self.odometer_reading) + ' miles on it.')
#   def update_odometer(self, mileage):
#     if mileage >= self.odometer_reading:
#       self.odometer_reading = mileage
#     else:
#       print('You can\'t roll back an odometer!')
#   def increment_odometer(self, miles):
#     self.odometer_reading += miles

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# # 修改属性的值
# # 直接修改
# my_new_car.odometer_reading = 23
# # 通过方法修改
# my_new_car.update_odometer(23)
# # 递增
# my_new_car.increment_odometer(5)

# 继承
## 汽车
# class Car():
#   def __init__(self, make, model, year):
#     self.make = make
#     self.model = model
#     self.year = year
#     self.odometer_reading = 0
#   def get_descriptive_name(self):
#     long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#     return long_name.title()
#   def read_odometer(self):
#     print('This car has ' + str(self.odometer_reading) + ' miles on it.')
#   def update_odometer(self, mileage):
#     if mileage >= self.odometer_reading:
#       self.odometer_reading = mileage
#     else:
#       print('You can\'t roll back an odometer!')
#   def increment_odometer(self, miles):
#     self.odometer_reading += miles

# ## 电动车
# class ElectricCar(Car):
#   def __init__(self, make, model, year):
#     super().__init__(make, model, year)
#     self.battery_size = 70
#   def describe_battery(self):
#     print('This car has a ' + str(self.battery_size) + '-kWh battery.')
#   # 在子类中定义与父类相同的方法将覆盖父类的方法，优先调用子类
#   def fill_gas_tank(self):
#     print('This car doesn\'t need a gas tank!')

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()

# 在其他文件中导入类：import car from Car

# Python 标准库
## 记录字典键值对的添加顺序
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jens'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'javascript'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
  print(name.title() + '\'s favorite language is ' + language.title() + '.')

