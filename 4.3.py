n = int(input())
a = 1
while n >= a:
    if a == n:
        print("YES")
    elif a * 2 > n:
        print("NO")
    a = a * 2
