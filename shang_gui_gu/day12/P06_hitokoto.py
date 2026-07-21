import requests

url = 'https://v1.hitokoto.cn/'

params = {
    "c": "f"
}

response = requests.get(url, params=params)

status_code = response.status_code

if status_code == 200:
    response_data = response.json()
    print(f"{response_data['hitokoto']} ---{response_data['from']}")
else:
    print('错误~')
