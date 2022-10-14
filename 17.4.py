def mean(*args):
    n = []
    for i in args:
        if type(i) == float or type(i) == int:
            n.append(i)
    if len(n) == 0:
        return float(sum(n))
    return sum(n)/len(n)


print(mean())
