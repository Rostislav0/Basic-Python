numbers = [1, 2, 3]
words = ['one', 'two', 'three']
romans = ['I', 'II', 'III']
for pair in zip(numbers, words, romans):
    print(pair)
for x, y in zip(numbers, words):
    print(x, y)

print()
result = zip(numbers, words, romans)
print(result)
print(list(result))


print()
keys = ['name', 'age', 'gender']
values = ['Timur', 28, 'male']

info = dict(zip(keys, values))
print(info)

print()
list1 = ['a1', 'a2', 'a3']
list2 = ['b1', 'b2', 'b3']

for index, (item1, item2) in enumerate(zip(list1, list2)):
    print(index, item1, item2)