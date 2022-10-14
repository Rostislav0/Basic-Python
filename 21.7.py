letters = {input():0 for _ in range(int(input()))}
for i in letters.keys():
    k = i.split('.')
    oad = 0
    e = 3
    for d in k:
        oad += int(d) * 256 ** e
        e -= 1
    letters[i] = oad

a = sorted(letters.items())
b = sorted(a, key=lambda x: x[1])
for i in b:
    print(i[0])