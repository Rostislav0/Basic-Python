n = int(input())
k = 1
d = 0
while k != n + 1:
    s = 1 / k ** 2
    d += s
    k += 1
print(d)
