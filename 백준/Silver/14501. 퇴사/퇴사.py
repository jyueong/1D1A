n = int(input())
info = []
dp = [0 for _ in range(n+1)]
max_p = 0

for _ in range(n):
    info.append(tuple(map(int, input().split())))

for i in range(n-1, -1, -1):
    if info[i][0] > n - i:
        dp[i] = max_p
    else:
        max_p = max(info[i][1]+dp[i+info[i][0]], max_p)
        dp[i] = max_p

print(dp[0])