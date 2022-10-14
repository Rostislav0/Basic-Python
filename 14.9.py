from decimal import *

num = Decimal('10.0')

print(num.sqrt())
print(num.exp())
print(num.ln())
print(num.log10())
print()
num = Decimal('-1.4568769017')
num_tuple = num.as_tuple()

print(num.as_tuple())
print(num_tuple.sign)
print(num_tuple.digits)
print(num_tuple.exponent)

print()
print(getcontext())
getcontext().prec = 3      # устанавливаем точность в 3 знака

num = Decimal('3.1415')

print(num)
print(num * 1)
print(num * 2)
print(num / 2)
print()
s = '1.34 3.45 1.00 0.03 9.25'

numbers = [Decimal(i) for i in s.split()]

maximum = max(numbers)
minimum = min(numbers)

numbers.sort()

print(maximum)
print(minimum)
print(numbers)
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))