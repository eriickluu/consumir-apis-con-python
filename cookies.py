import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/cookies'
    cookies = {
        'my-cookie': 'true'
    }
    response = requests.get(url, cookies=cookies)

    if response.ok:
        cookies = response.cookies
        print(cookies)

        print("El contenido es:")
        print(response.content)