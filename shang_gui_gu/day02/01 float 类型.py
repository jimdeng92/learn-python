from decimal import Decimal


f1 = 0.1
f2 = 0.2
f3 = f1 + f2

print(f3)  # 输出 0.30000000000000004
print(type(f3))  # 输出 <class 'float'>

d1 = Decimal('0.1')
d2 = Decimal('0.2')
d3 = d1 + d2

print(d3)  # 输出 0.3
print(type(d3))  # 输出 <class 'decimal.Decimal'>



