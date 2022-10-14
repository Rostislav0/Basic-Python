def sem(number):
    s = 0
    for num in number:
        s += int(num)
    return s


n = [int(i) for i in input().split()]
n.sort()
n1 = [str(i) for i in n]
n1.sort(key=sem)
print(*n1)
