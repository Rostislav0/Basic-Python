import requests
import string
URL = 'http://www.pythonchallenge.com/pc/def/equality.html'

r = requests.get(URL).text

n = 0

while n+8 != len(r):
    if r[n] in string.ascii_lowercase:
        if r[n+1] in string.ascii_uppercase:
            if r[n+2] in string.ascii_uppercase:
                if r[n+3] in string.ascii_uppercase:
                    if r[n+4] in string.ascii_lowercase:
                        if r[n + 5] in string.ascii_uppercase:
                            if r[n + 6] in string.ascii_uppercase:
                                if r[n+7] in string.ascii_uppercase:
                                    if r[n+8] in string.ascii_lowercase:
                                        print(r[n+4], end='')
                                    else:
                                        letters = ''
                                else:
                                    letters = ''
                            else:
                                letters = ''
                        else:
                            letters = ''
    n += 1


