n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
l, r, t, b = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if j < i < n - 1 - j:
            l += matrix[i][j]
        elif j > i > n - 1 - j:
            r += matrix[i][j]
        elif i < j and i < n - 1 - j:
            t += matrix[i][j]
        elif i > j and i > n - 1 - j:
            b += matrix[i][j]
print(f"Верхняя четверть: {t}",
      f"Правая четверть: {r}",
      f"Нижняя четверть: {b}",
      f"Левая четверть: {l}", sep='\n')
