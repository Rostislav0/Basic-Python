s1 = [set([int(i) for i in input().split()]) for _ in range(3)]
s2 = s1[0].union(s1[1], s1[2])
print(*sorted(set(range(11)).difference(s2)))
