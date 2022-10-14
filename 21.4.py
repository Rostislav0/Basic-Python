def check(num):
    a = [int(i) for i in str(num)]
    return all(list(map(lambda x: num % x == 0, a)))


full_numbers = list(range(int(input()), int(input())+1))
numbers_without_zero = []
for i in full_numbers:
    if '0' not in str(i):
        numbers_without_zero.append(i)
print(*list(filter(lambda x: x if check(x) is True else 0, numbers_without_zero)))
