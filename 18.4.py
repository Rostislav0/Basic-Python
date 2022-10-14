def sem(number):
    s = 0
    for num in number:
        s += int(num)
    return s


n = [str(i) for i in input().split()]
n1 = sorted(n, key=sem)
print(*n1)
