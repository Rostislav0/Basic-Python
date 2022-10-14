x = int(input())
x1 = x
while x1 != 0:
    x1 = int(input())
    if x1 > x and x1 != 0:
        x = x1
print(x)
