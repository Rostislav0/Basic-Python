def greet(name, *args):
    hi = f'Hello, {name}'
    for i in args:
        hi += f" and {i}"
    return hi + '!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
