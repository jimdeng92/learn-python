# 字典

# alien_0 = {'color': 'green', 'point': 5}

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)


# 删除键值对

# del alien_0['color']

# print(alien_0)

# 遍历字典

# user_0 = {
#   'username': 'efermi',
#   'first': 'enrico',
#   'last': 'fermi'
# }

# for key, value in user_0.items():
#   print('\nKey:' + key)
#   print('Value:' + value)

# 遍历字典的键

# favorite_languages = {
#   'jen': 'python',
#   'sarah': 'c',
#   'edward': 'ruby',
#   'phil': 'python'
# }

# for name in favorite_languages.keys():
#   print(name.title())

# 遍历字典的值

# favorite_languages = {
#   'jen': 'python',
#   'sarah': 'c',
#   'edward': 'ruby',
#   'phil': 'python'
# }

# for language in favorite_languages.values():
#   print(language.title())

# 去重
# for language in set(favorite_languages.values()):
#   print(language.title())

# 生成多个外星人

aliens = []
for alien_number in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

for alien in aliens[:5]:
  print(alien)

print('...')

print('Total number of aliens: ' + str(len(aliens)))

