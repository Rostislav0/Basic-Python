a = set(input().split())
b = set(input().split())
c = set(input().split())
d = sorted([int(i)for i in a.intersection(b).difference(c)])
for i in d[::-1]:
    print(i, end=' ')

