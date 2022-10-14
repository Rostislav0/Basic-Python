a = {}
b = {}

for i in range(int(input())):
    d = input().lower()
    a[d] = ''

for i in range(int(input())):
    k = input().lower().split()
    for v in k:
        b[v] = ''

for w in b.keys():
    if w not in a.keys():
        print(w)
