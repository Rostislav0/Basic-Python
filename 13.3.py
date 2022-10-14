import random
password = ''
for _ in range(int(input())):
    password += [str(random.randrange(9)), chr(random.randint(65, 90)), chr(random.randint(97, 122))][random.randint(0, 2)]
print(password)
