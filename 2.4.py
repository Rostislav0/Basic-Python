from decimal import Decimal

print("Значения от A")

F1 = Decimal(input("F1>>"))
MF1 = Decimal(input("MF1a>>"))
m = Decimal(input("m>>"))
F2 = Decimal(input("F2>>"))
MF2 = Decimal(input("MF2a>>"))
MRb = Decimal(input("MRb>>"))

total1 = (+ F1 * MF1 + m + F2 * MF2) / MRb
total2 = (+ F1 * MF1 + m - F2 * MF2) / MRb
total3 = (+ F1 * MF1 - m - F2 * MF2) / MRb
total4 = (- F1 * MF1 - m - F2 * MF2) / MRb
total5 = (- F1 * MF1 + m - F2 * MF2) / MRb
total6 = (- F1 * MF1 + m + F2 * MF2) / MRb
total7 = (- F1 * MF1 - m + F2 * MF2) / MRb
total8 = (+ F1 * MF1 - m + F2 * MF2) / MRb


print("Значения от B")

MF2a = Decimal(input("MF2b>>"))
MF1a = Decimal(input("MF1b>>"))


total1a = (+ F2 * MF2a + m + F1 * MF1a) / MRb
total2a = (+ F2 * MF2a + m - F1 * MF1a) / MRb
total3a = (+ F2 * MF2a - m - F1 * MF1a) / MRb
total4a = (- F2 * MF2a - m - F1 * MF1a) / MRb
total5a = (- F2 * MF2a + m - F1 * MF1a) / MRb
total6a = (- F2 * MF2a + m + F1 * MF1a) / MRb
total7a = (- F2 * MF2a - m + F1 * MF1a) / MRb
total8a = (+ F2 * MF2a - m + F1 * MF1a) / MRb


print()
print("Ra")
print(round(total1, 2))
print(round(total2, 2))
print(round(total3, 2))
print(round(total4, 2))
print(round(total5, 2))
print(round(total6, 2))
print(round(total7, 2))
print(round(total8, 2))

print("Rb")
print(round(total1a, 2))
print(round(total2a, 2))
print(round(total3a, 2))
print(round(total4a, 2))
print(round(total5a, 2))
print(round(total6a, 2))
print(round(total7a, 2))
print(round(total8a, 2))


calc1 = F1 + F2 - (round(total1a, 2))
calc2 = F1 + F2 - (round(total2a, 2))
calc3 = F1 + F2 - (round(total3a, 2))
calc4 = F1 + F2 - (round(total4a, 2))
calc5 = F1 + F2 - (round(total5a, 2))
calc6 = F1 + F2 - (round(total6a, 2))
calc7 = F1 + F2 - (round(total7a, 2))
calc8 = F1 + F2 - (round(total8a, 2))


print("Total")
print(calc1)
print(calc2)
print(calc3)
print(calc4)
print(calc5)
print(calc6)
print(calc7)
print(calc8)


print()

print("Ra")
print(round(total1, 2))
print(round(total2, 2))
print(round(total3, 2))
print(round(total4, 2))
print(round(total5, 2))
print(round(total6, 2))
print(round(total7, 2))
print(round(total8, 2))
