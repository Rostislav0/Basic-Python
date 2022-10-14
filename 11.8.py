s = set()
for i in [int(i) for i in input().split()]:
    if i in s:
        print("YES")
    else:
        s.add(i)
        print("NO")
