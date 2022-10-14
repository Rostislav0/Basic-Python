def pretty_print(data, side='-', delimiter='|'):
    l = 0
    l1 = 0
    for i in data:
        l += len(str(i)) + 2
        l1 += 1
    print('', side * (l + l1 - 1))
    for i in data:
        print(delimiter, i, end=' ')
    print(delimiter)
    print('', side * (l + l1 - 1))
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')