import requests
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse


async def get_hitokoto():
    try:
        params = {
            'c': 'b',
            'encode': 'json'
        }
        response = requests.get(url='https://v1.hitokoto.cn/', params=params)
        status_code = response.status_code

        if status_code == 200:
            json_data = response.json()
            return json_data
        else:
            return {'error': '请求失败~'}
    except requests.RequestException as e:
        return {'error': str(e)}

async def homepage(request):
    hitokoto = await get_hitokoto()
    return JSONResponse(hitokoto)

app = Starlette(debug=True, routes=[
    Route('/', homepage),
])

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
