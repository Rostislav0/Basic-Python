n = int(input())
a = [[0] * n for i in range(n)]
f = 1
y = 0  # номер строки
x = n - 1  # номер эллемента
for i in a:
    for n in range(len(i)):
        y += 1
        x += 1
        i[y][x] = f
        f += 1
    print(i)
print()
print(a)
