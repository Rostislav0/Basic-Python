b = [input() for i in range(int(input()))]
result = [set(b[-1])]
for i in b[0:-1]:
    result[0].intersection_update(set(i))
print(*sorted(*result))
