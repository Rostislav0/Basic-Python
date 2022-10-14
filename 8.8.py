i = int(input())
fr = {}
for x in range(i):
    d = input().split(';')
    if d[0] not in fr.keys():
        fr[d[0]] = [0, 0, 0, 0, 0]
    if d[2] not in fr.keys():
        fr[d[2]] = [0, 0, 0, 0, 0]

    if int(d[1]) > int(d[3]):
        fr[d[0]][1] = int(fr[d[0]][1]) + 1
        fr[d[2]][3] = int(fr[d[2]][3]) + 1
        fr[d[0]][4] = int(fr[d[0]][4]) + 3

    elif int(d[1]) < int(d[3]):
        fr[d[2]][1] = int(fr[d[2]][1]) + 1
        fr[d[0]][3] = int(fr[d[0]][3]) + 1
        fr[d[2]][4] = int(fr[d[2]][4]) + 3


    elif int(d[1]) == int(d[3]):
        fr[d[0]][2] = int(fr[d[0]][2]) + 1
        fr[d[2]][2] = int(fr[d[2]][2]) + 1
        fr[d[0]][4] = int(fr[d[0]][4]) + 1
        fr[d[2]][4] = int(fr[d[2]][4]) + 1


for x in fr.values():
    x[0] = sum(x[1:4])

for x, f in fr.items():
    print(x, ":", end='', sep='')
    print(*f, sep=' ')

