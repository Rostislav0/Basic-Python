t = input()
if t == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(float(a*b))
elif t == 'круг':
    r = int(input())
    print(float(3.14*r**2))
elif t == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = p*(p-a)*(p-b)*(p-c)
    print(s ** 0.5)
