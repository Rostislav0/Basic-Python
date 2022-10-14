myset1 = {1, 2, 3, 4}  # {1, 2, 3, 4}
myset2 = set()  # Пустое множество
myset3 = set('aaaabbbbcccddd')  # {'d', 'c', 'b', 'a'}
myset4 = {'aaa', 'bb', 'cc'}  # {'bb', 'cc', 'aaa'}
myset5 = set(range(10))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
myset6 = set('aaa bbbb cc')  # {' ', 'b', 'c', 'a'}
myset6.remove(' ')  # {'b', 'c', 'a'}

print(myset6)

myset7 = {1, 2, 2, 3, 3, 4, 4, 5, 5}  # {1, 2, 3, 4, 5}

myset8 = set('erer-aer')
print(myset8)

print(*sorted(myset7, reverse=True), sep='\n')

numbers = {1, 2, 3, 4, 5}

print('до удаления:', numbers)
num = numbers.pop()            # удаляет случайный элемент множества, возвращая его
print('удалённый элемент:', num)
print('после удаления:', numbers)

digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}
print(digits)