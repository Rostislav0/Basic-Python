x = [int(i) for i in input().split()]
a = set()
for i in x:
    if x.count(i) > 1:
        a.add(i)
print(*a)
