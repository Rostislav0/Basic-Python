import requests
from bs4 import BeautifulSoup

link = 'https://catalog.onliner.by/'

response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id="userbar")
a = block.find('a', href="https://profile.onliner.by")
print(a)