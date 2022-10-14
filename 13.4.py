import random
bil = []
for _ in range(7):
    bil.append(random.randint(1, 49))
print(*sorted(bil))
