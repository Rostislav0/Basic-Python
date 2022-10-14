n = int(input())
k = 0
x = 0
while k != n:
    k = k + 1
    x = x + k ** 2
    if n == k:
        print(x)
