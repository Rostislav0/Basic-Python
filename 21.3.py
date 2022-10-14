def check(ls):
    return any(list(map(lambda x: '5' in x, ls)))


a = [[[str(i) for i in input().split()] for d in range(int(input()))] for _ in range(int(input()))]
print("YES" if all(list(map(lambda x: check(x), a))) is True else "NO")
