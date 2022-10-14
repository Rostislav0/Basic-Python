import requests
from bs4 import BeautifulSoup

link = 'https://pythonworld.ru/moduli/modul-math.html'
response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id='content')
math = block.find('header')
math2 = math.find('h1').text
d = f'Заголовок: {math2}'
ceil = block.find_all('p')
print(d)

for c in ceil[1:]:
    print(c.text)



