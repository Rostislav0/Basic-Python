from functools import reduce

words = ['python', 'stepik', 'beegeek', 'iq-option']
numbers = [1, 2, 3, 4, 5, 6]

summa = reduce(lambda x, y: x + y, numbers, 0)
product = reduce(lambda x, y: x * y, numbers, 1)
sentence = reduce(lambda x, y: x + ' loves ' + y, words, 'Everyone')

print(summa)
print(product)
print(sentence)

print()

numbers = [-2, 0, 1, 2, 17, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0 and x != 2, numbers))
result2 = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
print(result)
print(result2)
