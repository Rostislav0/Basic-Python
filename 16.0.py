import string
s = '''map'''
a = []
n = -1
for i in s.split():
    n += 1
    for d in i:
        if d in string.ascii_lowercase:
            a.append([])
            x = ord(d)
            if x == 121:
                a[n] += 'a'
            elif x == 122:
                a[n] += 'b'
            else:
                a[n] += chr(x + 2)
        else:
            a[n] += d
for i in a:
    for d in i:
        print(d, end='')
    print(end=' ')
