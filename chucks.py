import requests
import json

if __name__ == '__main__':
    url = 'http://imgur.com/r/cats/n9z3sLg'

    response = requests.get(url, stream=True) # Realiza la petición sin descargar el contenido 
    
    with open('image.jpg', 'wb') as file:
        for chuck in response.iter_content(): # Descarga el contenido poco a poco 
            file.write(chuck)

    response.close()
