m = int(input())
p = set()
l = [{input() for i in range(int(input()))} for d in range(m)]
if m == 1:
    print(*sorted(l[0]), sep='\n')
else:
    for i in range(len(l)-1):
        if i == 0:
            p = l[i]
        p.intersection_update(l[i+1])
    print(*sorted(p), sep='\n')