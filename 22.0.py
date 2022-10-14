import string

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

x = input()
p = [i.upper() if i in string.ascii_letters else i for i in x]
s = {}
for i, e in list(zip(morse, letters)):
    s[e] = i
c = list(map(lambda x: s.get(x, ''), p))
while c.count('') != 0:
    c.remove('')
print(*c)
