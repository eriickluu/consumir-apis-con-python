import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    # url = 'http://httpbin.org/get?nombre=erick&curso=python'
    payload = {
        'name': 'Erick',
        'course': 'Python',
        'level': 'Intermedio'
    }

    # response = requests.post(url, json=payload)
    response = requests.post(url, data=json.dumps(payload))

    # json post se encarga de serializarlos 
    # data entonces nosotros nos encargamos de serializarlos
    print(response.url)

    if response.status_code == 200:
        print(response.content)