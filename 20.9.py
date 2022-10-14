abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]
R = 2
pr = list(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2, list(zip(abscissas, applicates, ordinates))))
print(all(list(map(lambda x: True if R**2 >= x else False, pr))))
