import requests
import json

if __name__ == '__main__':
    # url = 'http://httpbin.org/put'
    url = 'http://httpbin.org/delete'
    payload = {
        'name': 'Erick',
        'course': 'Python',
        'level': 'Intermedio'
    }

    headers = {
        'Conten-Type': 'application/json',
        'access_token': '12345'
    }

    # response = requests.put(url, data=json.dumps(payload), headers=headers)
    response = requests.delete(url, data=json.dumps(payload), headers=headers)
    """
    GET
    POST 
    PUT 
    DELETE
    """

    print(response.url)

    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers # Dic
        # print(headers_response)
        server = headers_response['server']
        print(server)