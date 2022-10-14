sec = int(input())

mm = sec // 60
h = mm // 60
sec3 = h * 3600
sec4 = sec - sec3
mm1 = sec4 // 60
sec5 = mm1 * 60
tsec = sec4 - sec5

print(h, end=':')


if mm1 < 10 and tsec < 10:
    print("0", end='')
    print(mm1, end=':')
    print("0", end='')
    print(tsec)

elif mm1 > 10 and tsec < 10:
    print(mm1, end=':')
    print("0", end='')
    print(tsec)

elif mm1 < 10 and tsec > 10:
    print("0", end='')
    print(mm1, end=':')
    print(tsec)

elif mm1 > 10 and tsec > 10:
    print(mm1, end=':')
    print(tsec)
