s = {'der', 'das', 'die'}


print(s)
print('der' in s)
print('deer' in s)

s.add('deer')
print('add>>', s)

s.remove('der')
print('remove>>', s)

s.discard('dear')
print('discard>>', s)

print(len(s))

s.clear()
print('clear>>', s)