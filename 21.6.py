letters = {input():0 for _ in range(int(input()))}
for i in letters.keys():
    sch = 0
    for l in i:
        sch += ord(str(l).upper()) - ord("A")
    letters[i] = sch
a = sorted(letters.items())
b = sorted(a, key=lambda x: x[1])
for i in b:
    print(i[0])
