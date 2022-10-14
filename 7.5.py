dir = {'a343a31': ['Иван', "Никита"],'b134i45': 'Петя', 'c313r51': 'Вася'}
f = 1
for i in dir.items():
    print(f, end=')')
    print(*i, sep=':')
    f += 1

print("КЛЮЧИ:")
for i in dir.keys():
    print(i, end='; ')
print("\nЗНАЧЕНИЯ:")
for i in dir.values():
    print(i, end='; ')