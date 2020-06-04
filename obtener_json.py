import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    # url = 'http://httpbin.org/get?nombre=erick&curso=python'
    args = {
        'name': 'Erick',
        'course': 'Python',
        'level': 'Intermedio'
    }

    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        # response_json = response.json() # Dic
        # origin = response_json['origin']
        # print(origin)

        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)