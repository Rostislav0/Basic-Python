print(("NO", "YES")[set(input()) == set(input()) == set(input())])  # with \n

# without \n
x = input().split()
print(("NO", "YES")[set(x[0]) == set(x[1]) == set(x[2])])

