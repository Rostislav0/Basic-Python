st1 = set([int(i) for i in input().split()])
st2 = set([int(i) for i in input().split()])
st3 = set([int(i) for i in input().split()])
st12 = st1.union(st2)
print(*sorted(st3.difference(st12), reverse=True))