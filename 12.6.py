a = set(input().split())
b = set(input().split())
c = set(input().split())
k = a.union(b, c)
d = a.intersection(b, c)
x = []
for i in (k - d):
    x.append(int(i))
print(*sorted(x))
