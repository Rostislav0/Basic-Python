from fractions import Fraction
import math
num1 = Fraction(5, 10)
num2 = Fraction('75/100')
num3 = Fraction('0.25')
print(num1, num2, num3)

num = Fraction('63/114')

print('Numerator of fraction equal:', num.numerator)
print('Denominator of fraction equal:', num.denominator)

print(num.as_integer_ratio())
print()

print('PI =', math.pi)
num = Fraction(str(math.pi))
print('No limit =', num)

for d in [1, 5, 50, 90, 100, 500, 1000000]:
    limited = num.limit_denominator(d)
    print(limited)


