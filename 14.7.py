from random import randint as r
from random import sample as sa
n, m = int(input()), int(input())
pa = ''
length = 0
for i in range(n):
    while len(pa) != m:
        if length == 0:
            pa += [chr(r(65, 72)), chr(r(74, 78)), chr(r(80, 90))][r(0, 2)]
            pa += [chr(r(97, 107)), chr(r(109, 110)), chr(r(112, 122))][r(0, 2)]
            pa += str(r(2, 9))
            length += 1
        if len(pa) == m:
            break
        pa += [chr(r(65, 72)), chr(r(74, 78)), chr(r(80, 90)), chr(r(97, 107)), chr(r(109, 110)),
               chr(r(112, 122)), str(r(2, 9))][r(0, 6)]
    length = 0
    print(''.join(sa(pa, len(pa))))
    pa = ''
