a = int(input())
b = int(input())
q = 0
d = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        q += 1
        d += i
print(d / q)
