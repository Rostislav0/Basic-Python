m = (int(input()))
num = 1
p = 0
n = [num]
d = []
while p != m:
    j = [n[p]]*num
    d.extend(j)
    num += 1
    p += 1
    n.append(num)
print(*d[:m])
