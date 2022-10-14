a = []
x = 0
y = 0

for i in range(int(input())):
    a.extend(input().split())
    if a[0] == 'юг':
        y -= int(a[1])
    elif a[0] == 'север':
        y += int(a[1])
    elif a[0] == 'запад':
        x -= int(a[1])
    elif a[0] == 'восток':
        x += int(a[1])
    a = []
print(x, y)
