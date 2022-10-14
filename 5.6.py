i = 0
h = 1
b = [1, 2, 3, 4, 5, 34]
while len(b) > 0:
    x = [b[i], '№', h]
    print(x)
    i += 1
    h += 1
    if i == len(b):
        break
print("YES")
