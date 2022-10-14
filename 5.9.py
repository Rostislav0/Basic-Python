n = int(input())
s = 0
for i in range(n):
    a = input()
    if a == 'x':
        break
    s += int(a)
    print('current:', s)
print("total:", s)
