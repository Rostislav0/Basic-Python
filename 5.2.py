A = float(input())
B = float(input())
while A != B:
    if A % 2 == 0:
        print(":2")
        A = A / 2
        continue
    else:
        print("-1")
        A = A - 1