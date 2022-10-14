n = input()
n += '.'
inf = len(n)
s1 = 0
s2 = 1
k = 0
for i in n:
    if s2 < inf:
        if n[s1] == n[s2]:
            k += 1
        else:
            print(i, k + 1, end='', sep='')
            k = 0
    s1 += 1
    s2 += 1
