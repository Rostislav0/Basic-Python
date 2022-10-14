def my_func(num, *args):
    print(args)
    print(num)


my_func(17, 'Python', 2, 'C#')
print()


def my_sum(*args):
    return sum(args)


print(my_sum())
print(my_sum(1))
print(my_sum(1, 2))
print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4))
print(my_sum(*[1, 2, 3, 4, 5]))  # распаковка списка
print(my_sum(*(1, 2, 3)))  # распаковка кортежа
print(my_sum(1, 2, *[3, 4, 5], *(7, 8, 9), 10))

print('\n\n')


def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
    print(a, b)
    print(args)
    print(name, age)
    print(kwargs)


my_func(1, 2, 3, 4, name='Timur', age=28, job='Teacher', language='Python')
my_func(1, 2, name='Timur', age=28, job='Teacher', language='Python')
my_func(1, 2, 3, 4, job='Teacher', language='Python')
