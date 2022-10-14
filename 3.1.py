x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x2 == x1 + 1 and y2 == y1 or x2 == x1 and y2 == y1 + 1 or\
        x2 == x1 + 1 and y2 == y1 + 1 or (x1 + y1 == x2 + y2) \
        and x1 + y1 + x2 + y2 != 18 or x1 + x2 != y1 + y2 or\
        x2 == x1 - 1 and y2 == y1 \
        or x2 == x1 and y2 == y1 - 1 or\
        x2 == x1 - 1 and y2 == y1 - 1:
    print("YES")
else:
    print("NO")
