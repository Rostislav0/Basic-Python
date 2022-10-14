b = []
gr1 = 0
gr2 = 0
gr3 = 0
col = 0
with open("8.2.txt", "r", encoding='utf-8') as lines:
    for line in lines:
        a = line.strip().split(';')
        for i in a[1:4]:
            b.extend([float(i)])
        col += 1
        gr1 += float(a[1])
        gr2 += float(a[2])
        gr3 += float(a[3])
        print(a[0], sum(b) / 3)
        b = []
print(gr1/col, gr2/col, gr3/col)
