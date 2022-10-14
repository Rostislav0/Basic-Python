colors = ['red', 3, 'blue', 'cyan']
a, _, c, d = colors
print(a)
print(_)
print(c)
print(d)


a, b, *tail = 1, 2, 3, 4, 5, 6
print(a, b)
print(tail)


singer = ('Freddie', 'Bohemian Rhapsody', 'Killer Queen', 'Love of my life', 'Mercury')
name, *songs, surname = singer
print(name)
print(songs)
print(surname)


s1 = 'abc-de'.partition('-')
s2 = 'abc-de'.partition('.')
s3 = 'abc-de-fgh'.partition('-')
s4 = s3[0:2] + s3[-1].partition('-')
print(s1)
print(s2)
print(s4)
