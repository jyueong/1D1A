N, K = map(int, input().split())

lst_A = list()

for _ in range(N):
    lst_A.append(int(input()))

ans = 0

while K != 0:
    coin = lst_A.pop()
    D, K = divmod(K, coin)
    ans += D

print(ans)