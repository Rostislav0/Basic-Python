import string


def check(func):
    return any(list(map(lambda x: x in func, password)))


up_l = string.ascii_uppercase
low_l = string.ascii_lowercase
num = string.digits
password = input()
print("YES" if all([check(up_l), check(low_l), check(num)]) is True and len(password) > 6 else "NO")
