i = int(input())
i1 = i
n = 0
while i1 != 0:
    i2 = int(input())
    if i2 == 0:
        break
    if i2 > i1:
        n += 1
        i1 = i2
    else:
        i1 = i2
        continue
print(n)
