# 创建和使用字典
person = {
    "name": "张三",
    "age": 18,
    "sex": "男",
    "height": 175,
    "weight": 75,
}
print(person)
print(len(person))
for key in person:
    print(key, person[key])

# 字典的运算
print(person["name"])
print(person.get("name"))
print(person.get('sex', '男'))
print('age' in person)
person['tel'] = "123456789"
print(person.keys())
print(person.values())
print(person.items())

for key, value in person.items():
    print(key, value)

person1 = {"name": "张三", "age": 18, "sex": "男", "height": 175, "weight": 75}
person2 = {"name": "李四", "age": 19, "sex": "女", "tel": "987654321"}
person1.update(person2)
print(person1)
print(person1.pop("tel"))
person1.clear()
print(person1)

# 输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出。
text = input("请输入一段话：")
counter = {}
for char in text:
    if char.isalpha():
        counter[char] = counter.get(char, 0) + 1

sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

for char, count in sorted_counter:
    print(f"{char}: {count}")


# 在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
stocks = {
    "000001": 10.23,
    "000002": 15.45,
    "000003": 20.67,
    "000004": 30.89,
    "000005": 40.12,
    "000006": 50.34,
    "000007": 60.56,
    "000008": 70.78,
    "000009": 80.90,
    "000010": 90.11,
    "000011": 100.12,
    "000012": 110.13,
    "000013": 120.14,
    "000014": 130.15,
    "000015": 140.16,
}
high_stocks = {code: price for code, price in stocks.items() if price > 100}
print(high_stocks)
