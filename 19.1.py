def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result


def square(x):
    return x**2


def cube(x):
    return x**3


numbers = [1, 2, -3, 4, -5, 6, -9, 0]

strings = map(str, numbers)        # используем в качестве преобразователя - функцию str
abs_numbers = map(abs, numbers)    # используем в качестве преобразователя - функцию abs

squares = map(square, numbers)     # используем в качестве преобразователя - функцию square
cubes = map(cube, numbers)         # используем в качестве преобразователя - функцию cube

print(strings)
print(abs_numbers)
print(squares)
print(cubes)
