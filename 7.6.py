f = {}


def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    elif key * 2 in d.keys():
        d[key*2].append(value)
    elif key * 2 not in d.keys():
        d[key*2] = [value]


print(update_dictionary(f, 1, -1))
print(f)
update_dictionary(f, 2, -2)
print(f)
update_dictionary(f, 1, -3)
print(f)
update_dictionary(f,5,7)
print(f)