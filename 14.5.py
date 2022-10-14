from string import *
from random import randint as r
n, m = int(input()), int(input())
pa = ''.join((set(ascii_letters).union(set(digits))).difference(set('lI1oO0')))
pe = ''
for i in range(n):
    while len(pe) != m:
        pe += pa[r(0, 55)]
    print(pe)
    pe = ''
