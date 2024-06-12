import sys

input = sys.stdin.readline

U, N = map(int, input().split())
price_dict = dict()

for i in range(N):
    x, y = input().split()
    price_dict[y] = price_dict.get(y, list()) + [x]

min_ppl = min([len(i) for i in price_dict.values()])
min_price = min([int(i) for i in price_dict.keys() if len(price_dict[i]) == min_ppl])

print(price_dict[str(min_price)][0], min_price)