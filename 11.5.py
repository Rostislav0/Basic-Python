a = []
for i in range(int(input())):
    x = set(input().lower())
    a.extend(x)
print(len(set(a)))
