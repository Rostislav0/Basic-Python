f = [1, 1, 1]
n1 = 0
n3 = 2
n = 4
l = int(input())
while n != 101:
    f.append(sum(f[n1:n3+1]))
    n += 1
    n1 += 1
    n3 += 1
print(*f[:l])
