a = []
tab = {str(i): [0, 0] for i in range(1, 12)}
with open("9.6.txt", 'r', encoding='utf-8') as f:
    for v in f.readlines():
        a.append(v.split())
        if a[0][0] in tab.keys():
            tab[a[0][0]][1] += 1
        tab[a[0][0]][0] += float(a[0][2])
        a = []

for k, v in tab.items():
    if v[0] == 0:
        tab[k] = '-'
    else:
        tab[k] = v[0] / v[1]

for k, v in tab.items():
    print(k, v)
