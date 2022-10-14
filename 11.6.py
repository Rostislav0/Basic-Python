x = input().lower().split()
a = []
for i in x:
    a.append(i.strip(".,;:-?!"))
print(len(set(a)))

