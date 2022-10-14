import random
bing = set()
while len(bing) != 25:
    bing.add(random.randint(1, 75))
bing = list(bing)
random.shuffle(bing)
bing[12] = 0
a1 = 0
a2 = 5
for i in range(5):
    print(*bing[a1:a2])
    a1 += 5
    a2 += 5

