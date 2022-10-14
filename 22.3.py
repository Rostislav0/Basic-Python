# prices
with open('test.txt', 'r', encoding='utf-8') as f:
    print(sum(map(lambda x: int(x.rstrip().split()[1]) * int(x.rstrip().split()[2]), f.readlines())))
