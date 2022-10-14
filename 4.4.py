x = int(input())
y = int(input())
c = 1
while y > x:
    c = c + 1
    x = x * 0.1 + x
print(c)
