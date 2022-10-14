def evaluate(coeff, x):
    for i in range(len(coeff)):
        coeff[i] = int(coeff[i])
    coeff = coeff[::-1]
    s = 1
    su = 0
    for i in coeff[1:]:
        su += i * (x ** s)
        s += 1
    return su + coeff[0]


print(evaluate(input().split(), int(input())))
