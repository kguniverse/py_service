import aiohttp
import asyncio
import json


async def main(params):
    async with aiohttp.ClientSession('http://127.0.0.1:1337') as session:
        async with session.get('/data', params = params) as response:
            form = params.get('form', 'json')
            if form == 'json':
                json_str = await response.json()
                str = json.dumps(json_str, indent=4, sort_keys=True)
                print(str)
            else:
                print(await response.text())


def test():
    key = input('input keyword (Temparature/[Year]):')
    if key == '':
        key = 'Year'
    reverse = input('want reverse sort \? (y/[N]):')
    if reverse == 'y':
        reverse = 'True'
    form = input('form \? (csv/xml/[json]):')
    if form == '':
        form = 'json'
    params = {'key': key, 'reverse': reverse, 'form': form}
    return params
loop = asyncio.get_event_loop()
loop.run_until_complete(main(test()))