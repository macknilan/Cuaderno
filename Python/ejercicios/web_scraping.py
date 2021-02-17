#
# requirements.txt
# requests==2.13.0
# beautifulsoup4==4.5.3
#
# Para los que están usando Python 3, ya no está disponible la librería urllib. Esta fue divida en varios módulos. El equivalente con Python 3 es lo siguiente:
# import urllib.request
# ...
# ...
# urllib.request.urlretrieve('https:{}'.format(image_url), image_name)
# http://stackoverflow.com/questions/17960942/attributeerror-module-object-has-no-attribute-urlretrieve
# https://docs.python.org/3.0/library/internet.html

import requests
from bs4 import BeautifulSoup
import urllib


def run():
    for i in range(1, 1501):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print('Descargando la imagen {}'.format(image_name))
        urllib.urlretrieve('https:{}'.format(image_url), image_name)


if __name__ == '__main__':
    run()
