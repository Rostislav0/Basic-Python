numbers = [int(input())]
now2 = 0
while sum(numbers) != 0:
    numbers.append(int(input()))
for a in numbers:
    now = a ** 2
    now2 += now
print(now2)
