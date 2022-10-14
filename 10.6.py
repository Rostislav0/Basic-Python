n, m, k, x, y, z = [int(input()) for _ in range(6)]

n -= x
m = m - x - y
k -= y

s = n + m + k + x + y + z
print(s)
