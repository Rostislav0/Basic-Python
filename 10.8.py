n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))

x = n + m - x - t
y = m + k - y - t
z = k + n - z - t
n = n - x - t - z
m = m - x - t - y
k = k - z - t - y

s = n + m + k + z + t + y + x

v1 = n + m + k
v2 = x + y + z
v3 = a - s

print(v1, v2, v3, sep='\n')
