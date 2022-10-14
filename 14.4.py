import random
a = {}
for i in range(int(input())):
    a[input()] = ''

b = [str(i) for i in a]

for i in a:
    x = random.choice(b)
    while i == x:
        if i == list(a.keys())[-1]:
            break
        else:
            x = random.choice(b)
    a[i] = x
    b.remove(x)
c = []
if list(a.keys())[-1] == list(a.values())[-1]:
    c.append(list(a.values())[-2])
    a[list(a.keys())[-2]] = list(a.values())[-1]
    a[list(a.keys())[-1]] = c[0]
for i, n in a.items():
    print(f"{i} - {n}")
