import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
responce = requests.get(url).text

strip = 'We'

while responce.strip().split()[0] != strip:
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + responce
    responce = requests.get(url).text
    print(responce)