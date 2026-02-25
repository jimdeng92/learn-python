"""
分支结构
"""

height = float(input('请输入您的身高（CM）:'))
weight = float(input('请输入您的体重（KG）:'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')

if 18.5 <= height < 24:
    print('您的体重属于标准范围')
elif bmi < 18.5:
    print('体重过轻')
else:
    print('过重')