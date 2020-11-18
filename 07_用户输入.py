# message = input('Tell me something, and I will repeat it back to you:')

# print(message)

# 字符串转数字

# prompt = 'How old are you?\n'

# age = input(prompt)

# age = int(age)

# print(age >= 18)

# 求模

# print(4 % 3)

# while 语句

# current_number = 1

# while current_number <= 5:
#   print(current_number)
#   current_number += 1

# prompt = '\nTell me something, add I will repeat it back to you.'
# prompt += '\nEnter "quit" to end the program.'

# active = True

# while active:
#   message = input(prompt)
#   if message == 'quit':
#     active = False
#   else:
#     print(message)

# break 和 continue
# break 终止循环
# continue 终止当前变量的循环，进入下一个变量的循环

# 打印奇数
number = 0
while number < 10:
  number += 1
  if number % 2 == 0:
    continue
  print(number)
  
