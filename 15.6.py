from fractions import Fraction as Fr
from math import *
# First way
count = 0
for i in range(1, int(input()) + 1):
    count += Fr(1, factorial(i))
print(count)
# Second way
print(sum([Fr(1, factorial(i)) for i in range(1, int(input()) + 1)]))
