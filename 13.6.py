import random
def generate_ip():
    ip = []
    it = ''
    for i in range(4):
        ip.append(str(random.randint(0, 255)))
        ip.append('.')
    ip.pop(-1)
    for i in ip:
        it += i
    return it

print(generate_ip())
