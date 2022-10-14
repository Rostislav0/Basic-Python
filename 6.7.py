i = []
n1 = 1
n0 = -1
for a in input().split():
    i.append(int(a))
for d in i:
    if n1 >= len(i):
        if len(i) == 1:
            print(i[0])
            break
        else:
            s = i[0] + i[n0]
            print(s, end=' ')
            break
    else:
        s = i[n0] + i[n1]
        n1 += 1
        n0 += 1
        print(s, end=' ')
