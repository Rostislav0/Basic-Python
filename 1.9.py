n = int(input())

sec = str(n % 60 // 10) + str(n % 60 % 10)
min = str(n // 60 % 60 // 10) + str(n // 60 % 10)
hour = str(n // 60 // 60 % 24)

print(hour, min, sec, sep=':')
