z1 = 5 + 7j
z2 = 1j
z3 = -3 + 5J
z4 = 1.5 + 3.2j

print(z1, z2, z3, z4, sep='\n')
print()
print(type(z1))
z1 = -3 + 2j              # создание на основе литерала
z2 = complex(6, -8)       # z2 = 6 - 8j
z3 = complex(0, 2.5)      # z3 = 2.5j
z4 = complex(5, 0)        # z4 = 5 + 0j
z5 = complex('3+4j')      # создание на основе строки

print(z1, z2, z3, z4, z5, sep='\n')
print()
import cmath

z = 2+3j
print(cmath.phase(z)) # полярный угол
print(cmath.polar(z)) # полярные координаты

