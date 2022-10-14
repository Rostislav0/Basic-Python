# trip.txt - table

with open('trip.txt', 'r', encoding='utf-8') as f:
    for d in list(map(lambda x: x.strip().split(' | ')[1:], f.readlines())):
        print('(', end='')
        for v in d[:-1]:
            print((lambda x: x if x.isdigit() or x == 'null' else f"'{x}'")(v), end=', ')
        print(*([f"'{d[-1]}'),"],[f"{d[-1]}),"])[d[-1] == 'null'])

