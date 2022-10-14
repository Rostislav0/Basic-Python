# count time of users action

with open('test.txt', 'r', encoding='utf-8') as f, open('test2.txt', 'w', encoding='utf-8') as f1:
    z = map(lambda x: x.rstrip().split(', '), f.readlines())
    c = list(filter(lambda x: abs((int(x[1][:2])*60 + int(x[1][3:]) - (int(x[2][:2])*60 + int(x[2][3:])))) >= 60, z))
    print(*list(map(lambda x:x[0], c)), sep='\n', file=f1)
