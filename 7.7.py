with open('7.7.txt') as inf:
    a1 = inf.readline()
    a2 = inf.readline()
# close

print(a1)
print(a2)
print(">>>")


with open("7.7.txt", 'w') as ouf:
    ouf.write("Some number\n")
    ouf.write(str(421))


with open("7.7.txt") as inf:
    for line in inf:
        line = line.strip()
        print(line)
