cod = input()
shr = input()
text = input()
out = input()

sl = {}
n = 0
intext = ''
inout = ''

for b in cod:
    sl[b] = shr[n]
    n += 1

for b in text:
    intext += sl[b]

for s in out:
    for k, v in sl.items():
        if v == s:
            inout += k

print(intext)
print(inout)
