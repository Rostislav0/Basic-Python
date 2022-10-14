import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()

link = 'https://account.habr.com/ajax/login/'

user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

data = {
    'login': 'rostik.1.2@mail.ru',
    'password': '9FDK82LD96'
}

respance = session.post(link, data = data, headers=header)


profile_info = 'https://profile.onliner.by/'
profile_response = requests.get(link).text
profile_soup = BeautifulSoup(profile_response, 'lxml')
profile_block = profile_soup.find()

print(profile_response)

