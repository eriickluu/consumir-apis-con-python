import requests

if __name__ == '__main__':
    url = 'https://www.google.com/'

    response = requests.get(url)

    if response.status_code == 200:
        # print(response.content)
        content = response.content
        file = open('google.html', 'wb')
        file.write(content)
        file.close()
        