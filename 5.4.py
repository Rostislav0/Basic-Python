a = []
kol = 1
i = float(input("Введите значение>>"))
n = i
a.append(i)
while n != 'x':
    n = str(input(str()))
    if n != 'x':
        a.append(float(n))
    else:
        break
while 1 > 0:
    print("Текущие значения>>", a, sep="---")
    v = int(input("Какое число вывести?>>"))
    print(a[v - 1])
    info = input("Что сделать?>>")
    if info == ':':
        d = float(input("На сколько разделить?>>"))
        a.append(a[v - 1] / d)
        print(a[-1])
        continue
    elif info == '*':
        u = float(input("На сколько умножить?"))
        a.append(a[v - 1] * u)
        print(a[-1])
        continue
    elif info == '+':
        s = float(input("Сколько прибавить?"))
        a.append(a[v - 1] + s)
        print(a[-1])
        continue
    elif info == '-':
        r = float(input("Сколько отнять?"))
        a.append(a[v - 1] - r)
        print(a[-1])
        continue
    else:
        print("Не известная команда...")
        continue
