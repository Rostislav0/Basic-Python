a = int(input())
b = []
while a / 10 > 1:
    x = a % 10
    b.append(x)
    a = a // 10
b.append(a)
print(''.join(map(str, b)))
