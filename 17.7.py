def info_kwargs(**kwargs):
    dictionary = sorted(kwargs)
    for beavers in dictionary:
        print(f"{beavers}:", kwargs[beavers])


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
