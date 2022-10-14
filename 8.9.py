i = int(input())
score = {}
for x in range(i):
    d = input().split(';')
    if d[0] not in score.keys():
        score[d[0]] = [0, 0, 0, 0, 0]
    if d[2] not in score.keys():
        score[d[2]] = [0, 0, 0, 0, 0]
    if int(d[1]) > int(d[3]):
        score[d[0]][1] += 1
        score[d[2]][3] += 1
    elif int(d[1]) < int(d[3]):
        score[d[2]][1] += 1
        score[d[0]][3] += 1
    else:
        score[d[0]][2] += 1
        score[d[2]][2] += 1
for x in score.values():
    x[0] = sum(x[1:4])
    x[4] = x[1] * 3 + x[2] * 1
for x, f in score.items():
    print(x, ":", end='', sep='')
    print(*f, sep=' ')
