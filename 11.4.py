a = []
for i in range(int(input())):
    x = len(set(input().lower()))
    a.append(x)
print(*a, sep='\n')
