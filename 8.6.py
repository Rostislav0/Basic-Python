import requests

url = 'https://stepic.org/media/attachments/course67/3.6.2/819.txt'
response = requests.get(url)
k = 0
for i in response.text.splitlines():
    k += 1
print(k)