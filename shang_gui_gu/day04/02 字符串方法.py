str1 = 'Hello world!'

print(str1.find('world'))  # 输出 6
print(str1.rfind('world'))  # 输出 6
print(str1.count('o')) # 输出 2
print(str1.upper()) # 输出 HELLO WORLD!
print(str1.lower()) # 输出 hello world!
print(str1.capitalize()) # 输出 Hello world!
print(str1.title()) # 输出 Hello World!
print(str1.replace('world', 'python')) # 输出 Hello python!
print(str1.strip()) # 输出 Hello world!
print(str1.lstrip()) # 输出 Hello world!
print(str1.rstrip()) # 输出 Hello world!
print(str1.startswith('Hello')) # 输出 True
print(str1.endswith('world!')) # 输出 True
print(str1.split(' ')) # 输出 ['Hello', 'world!']
print('_'.join(['a', 'b', 'c'])) # 输出 a_b_c
print(str1.center(20)) # 输出 ' Hello world! '
print(str1.ljust(20)) # 输出 ' Hello world! '
print(str1.rjust(20)) # 输出 ' Hello world! '
print(str1.zfill(20)) # 输出 '0000000Hello world!'
print(str1.encode()) # 输出 b'Hello world!'
print(str1.swapcase()) # 输出 hELLO WORLD!
print(str1.isalpha()) # 输出 False
print(str1.isdigit()) # 输出 False
print(str1.isalnum()) # 输出 False
print(str1.isspace()) # 输出 False
print(str1.islower()) # 输出 True
print(str1.isupper()) # 输出 False
print(str1.istitle()) # 输出 False
print(str1.isnumeric()) # 输出 False
print(str1.isdecimal()) # 输出 False


