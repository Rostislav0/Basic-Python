import requests

URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

numbers = '63579'
n = 0

while 'Yes.' not in requests.get(URL+numbers).text:
    response = requests.get(URL+numbers).text
    print(response)
    numbers = ''
    n += 1
    for i in response:

        if i.isdigit() == True:
            numbers += i
    print(n)
print(requests.get(URL+numbers).text)