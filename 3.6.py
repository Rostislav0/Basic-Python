x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
    print("YES")  # 1
elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
    print("YES")  # 2
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print("YES")  # 3
elif x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0:
    print("YES")  # 4
else:
    print("NO")
