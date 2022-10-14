with open('test.txt', 'r') as f1, open("test2.txt", "w") as f2:
    a = {}
    v = f1.read().split('GOATS')
    l1 = v[0].split('\n')[1:-1]
    l2 = v[1].split('\n')[1:]
    print(*sorted(filter(lambda x: round(l2.count(x) / len(l2) * 100, 2) > 7, l1)), sep='\n', end='', file=f2)
