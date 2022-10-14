import math

k = int(input())
m = int(input())
n = int(input())
col = n / k
total = math.ceil(col) * 2 * m
if n % k == 0:
    print(total)
else:
    print(total - 1)
