N = int(input())

lst = list()
ans = 0
max_profit = 0

for i in range(N):
    pay, cost = map(int, input().split())
    if pay > cost:
        lst.append([pay, cost])

lst = sorted(lst, key=lambda x: x[0])

L = len(lst)

for i in range(L):
    price = lst[i][0]
    profit = 0
    for j in range(L):
        np = price - lst[j][1]
        if price > lst[j][0]:
            continue
        elif np > 0:
            profit += np
    if profit > max_profit:
        max_profit = profit
        ans = price

print(ans)