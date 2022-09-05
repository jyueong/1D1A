a, b, c = map(int, input().split())

mu = c - b

if mu <= 0:
    print(-1)
else:
    print(int(a / mu) + 1)