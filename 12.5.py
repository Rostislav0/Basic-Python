items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
print(*sorted({int(i) for i in items}))



words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry',
         'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
a = []
for i in words:
    a.append(i[0].lower())
print(*sorted(set(a)))



sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
s = set()
for i in sentence.split():
    if len(i.strip(".,;:-?!()")) < 4:
        s.add(i.strip(".,;:-?!()").lower())
print(*sorted(s))



files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
s = set()
for i in files:
    if '.png' in i.lower():
        s.add(i.lower())
print(*sorted(s))
