# s1 = '\it \is \time \to \read \now'
# s2 = r'\it \is \time \to \read \now'
# print(s1)
# print(s2)

# 拼接和重复
s1 = 'hello'
s2 = 'world'
print(s1 + s2)
print(s1 * 3)

# 字符串切片
s = 'hello world'
print(s[0])
print(s[0:5])
print(s[6:])
print(s[:5])
print(s[:])
print(s[::2])
print(s[::-1])
print(s[0:10:2])
print(s[0:10:-1])

# 字符串格式化
name = 'Alice'
age = 18
print('My name is %s and I am %d years old.' % (name, age))
print('My name is {} and I am {} years old.'.format(name, age))
print(f'My name is {name} and I am {age} years old.')

# 字符串方法
s = 'hello world'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.center(20))
print(s.ljust(20))
print(s.rjust(20))
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace('hello', 'hi'))
print(s.split())
print(' '.join(s))
print(s.startswith('hello'))
print(s.endswith('world'))
print(s.find('world'))
print(s.count('o'))
print(s.index('world'))
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.isspace())
print(s.isnumeric())
print(s.isdecimal())
print(s.isidentifier())
print(s.isprintable())
print(s.istitle())
