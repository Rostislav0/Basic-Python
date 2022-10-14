a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
for i in range(b1, b2 + 1):
    print('\t\t', i, end=' ')
print()
for i in range(a1, a2 + 1):
    print(i, end=' ')
    for k in range(b1, b2 + 1):
        if k * i > 9:
            print('\t\t', k * i, end='')
        else:
            print('\t\t', k * i, end=' ')
    print()
