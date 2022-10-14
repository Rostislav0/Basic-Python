n = int(input())
if 10 < n < 20 or n > 100 and (n / 10) % 10 == 1:
    print(n, "программистов")
else:
    if 1 < n % 10 < 5:
        print(n, 'программиста')
    elif n % 10 == 1:
        print(n, "программист")
    else:
        print(n, "программистов")
