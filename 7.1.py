a = [12, 45, 52, 123]


def min2(n):
    m = n[0]
    for x in n:
        if m > x:
            m = x
    return m


def max2(d):
    s = d[0]
    for x in d:
        if s < x:
            s = x
    return s


print("MIN>>", min2(a))
print("MAX>>", max2(a))
