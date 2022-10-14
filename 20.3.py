mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
letters = []


mixed_list = sorted(mixed_list, key=lambda x: x if isinstance(x, int) else -1)
print(*sorted(mixed_list, key=lambda x: x if isinstance(x, str) else ''))
print(*sorted(mixed_list, key=str))