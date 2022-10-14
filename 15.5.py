from fractions import Fraction as Fr
# First way
count = 0
for i in range(1, int(input()) + 1):
    count += Fr(1, i ** 2)
print(count)
# Second way
print(sum([Fr(1, i ** 2) for i in range(1, int(input()) + 1)]))
