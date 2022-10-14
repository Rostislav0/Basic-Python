a = [[str(i) for i in input().split()] for d in range(int(input()))]
o = []
for i in a:
    i[1] = int(i[1])
    print(*i)
    if i[1] > 3:
        o.append(i)
print()
for i in o:
    print(*i)
