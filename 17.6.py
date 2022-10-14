def print_products(*args):
    products = []
    for i in args:
        if type(i) is str and len(i) > 1:
            products.append(i)
    if len(products) < 1:
        return print("Нет продуктов")
    n = 1
    for i in products:
        print(f"{n}) {i}")
        n += 1
    return 0


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
