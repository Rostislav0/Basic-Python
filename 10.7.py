a = []
b = []
c = []
for i in input().split():
    a.append(int(i))
for i in a:
    if i in b:
        pass
    else:
        b.append(i)
        a.remove(i)
for i in b:
    if i in a:
        c.append(i)
if len(c) <= 0:
    print('')
else:
    print(a)
    print(b)
    print(*c)
#  Решить словарём
