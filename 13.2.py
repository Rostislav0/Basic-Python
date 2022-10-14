import random

n = int(input())    # количество попыток
for i in range(n):
  print(["1","2","3","4","5","6"][random.randint(0,5)])