rub = int(input())
cent = int(input())
n = int(input())
rub_C = rub * 100
total = rub_C + cent
cost = total * n
print(cost // 100, cost % 100)
