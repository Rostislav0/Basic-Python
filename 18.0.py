numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(max(numbers, key=abs))
print(min(numbers, key=abs))  # указываем функцию abs в качестве компаратора
print(sorted(numbers, key=abs))

print()
def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a*x**2 + b*x + c
    return square_polynom

f = generator_square_polynom(a=1, b=2, c=1)
g = generator_square_polynom(a=2, b=0, c=-3)
h = generator_square_polynom(a=-3, b=-10, c=50)

print(f(1))
print(g(2))
print(h(-1))