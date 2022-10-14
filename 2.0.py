h1 = int(input())
mm1 = int(input())
sec1 = int(input())
h2 = int(input())
mm2 = int(input())
sec2 = int(input())

tsec1 = h1 * 3600 + mm1 * 60 + sec1
tsec2 = h2 * 3600 + mm2 * 60 + sec2
result = tsec2 - tsec1
print(result)
