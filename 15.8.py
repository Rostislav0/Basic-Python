from fractions import Fraction
s = int(input())
answer = set()
for den in range(1, s + 1):
    for nu in range(1, den):
        answer.add(Fraction(nu, den))
a = [i for i in answer]
a.sort()
[print(i) for i in a]

