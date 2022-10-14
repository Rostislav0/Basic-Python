numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
numbers = list(numbers)
n = 0
for i in numbers:
    i = list(i)
    numbers[n] = sum(i) / len(i)
    n += 1
print(numbers)