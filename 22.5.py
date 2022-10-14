with open('test.txt', 'w', encoding='utf-8') as f:
    x = [input() for _ in range(int(input()))]
    for i in x:
        with open(i, 'r', encoding='utf-8') as f1:
            print(f1.read(), file=f)
