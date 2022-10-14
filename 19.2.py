from operator import *
print(add(10, 20), 'sum')
print(truediv(20, 11), 'divide')
print(floordiv(20, 11), 'divide integer')
print(neg(9), 'change sign')
print(lt(2, 3), 'check <')
print(gt(10, 8), 'check >')
print(eq(5, 5), 'check isqualse')
print(ne(5, 9), 'difference')
print(pow(5, 3), 'Exponentiation **')
print()

pets = ['alfred', 'tabitha', 'william', 'arla']
chars = ['x', 'y', '2', '3', 'a']

uppered_pets = list(map(str.upper, pets))
capitalized_pets = list(map(str.capitalize, pets))
only_letters = list(filter(str.isalpha, chars))

print(uppered_pets)
print(capitalized_pets)
print(only_letters)