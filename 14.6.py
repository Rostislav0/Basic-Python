from random import randint as r
n, m = int(input()), int(input())
pa = ''
for i in range(n):
    while len(pa) != m:
        pa += [chr(r(65, 72)), chr(r(74, 78)), chr(r(80, 90)), chr(r(97, 107)), chr(r(109, 110)),
               chr(r(112, 122)), str(r(2, 9))][r(0, 6)]
    print(pa)
    pa = ''
