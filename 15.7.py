from fractions import Fraction
from math import *
s = int(input())
answer = 0
for nu in range(1, s-1):
    for den in range(1, s):
        if nu + den == s and gcd(nu, den) == 1 and nu < den:
            if Fraction(nu, den) > answer:
                answer = Fraction(nu, den)
print(answer)
