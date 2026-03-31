# name = input('请输入您的姓名：')
#
# print('原神欢迎您~，' + name)

print('hello', end=' ')
print('world')

int1 = 10
float1 = 1.2
bool1 = True

print(f'int1: {int1}, float1: {float1}, bool1: {bool1}')


"""
* 以*号填充
^ 居中 > 右对齐 < 左对齐
20 表示总宽度为20
, 表示用逗号分隔
.2f 表示小数点后保留两位
"""
print('{:*>20,.2f}'.format(int1))
print(f'{float1:*^20,.2f}')

