i = int(input())
i1 = i
if i1 % 2 == 0:
    n = 1
else:
    n = 0
while i1 != 0:
    i1 = int(input())
    if i1 % 2 == 0:
        n += 1
    else:
        continue
print(n-1)
