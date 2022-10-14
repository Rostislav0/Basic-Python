lst = [32, 3, 17, 16, 8]


def modify_list(l):
    b = []
    for i, n in enumerate(l):
        if n % 2 == 0:
            b.append(int(n / 2))
    l.clear()
    for f in b:
        l.append(int(f))
    return l


modify_list(lst)
print(lst)


