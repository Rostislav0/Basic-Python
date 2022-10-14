from random import randint as r
def generate_index():
    return f'{chr(r(65, 90))}{chr(r(65, 90))}{r(0, 99)}_{r(0, 99)}{chr(r(65, 90))}{chr(r(65, 90))}'
