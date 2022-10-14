def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    a = []
    for i in range(n):
        a.append([])
        for _ in range(m):
            a[i].append(value)
    return a


print(matrix())
print(matrix(3))
print(matrix(2, 5))
print(matrix(3, 4, 9))
