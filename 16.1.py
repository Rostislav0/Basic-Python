import requests
import string

URL = "http://www.pythonchallenge.com/pc/def/ocr.html"

response = requests.get(URL).text
for i in response:
    if i in string.ascii_letters or i == ' ':
        print(i, end='')
