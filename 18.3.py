import math

x = float(input())

dictionary = {'квадрат': x ** 2, 'куб': x ** 3, 'корень': x ** 0.5, 'модуль': abs(x), 'синус': math.sin(x)}
print(dictionary[input()])
