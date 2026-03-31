str1 = '你好世界~'

b1 = str1.encode(encoding='utf-8')

print(b1) # 输出: b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c~'
print(type(b1)) # 输出: <class 'bytes'>

str2 = b1.decode(encoding='utf-8')

print(str2) # 输出: 你好世界~


