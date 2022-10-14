x = input()
if len(x) == len(set(x)):
    print("YES")
else:
    print("NO")

# or

a = input()
print(('NO', 'YES')[len(a) == len(set(a))])  # NO = 0, YES = 1. If true - is 1, else - 0
