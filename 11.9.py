myset1 = set(range(10))
myset2 = set(range(7, 12))
print(myset1.union(myset2))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print(myset1.difference(myset2))  # {0, 1, 2, 3, 4, 5, 6}
print(myset1.symmetric_difference(myset2))  # {0, 1, 2, 3, 4, 5, 6, 10, 11}
myset1.intersection_update(myset2)
print(myset1)  # {8, 9, 7}
myset3 = set(range(4))
print(myset1.union(myset2, myset3))  # {0, 1, 2, 3, 7, 8, 9, 10, 11}
