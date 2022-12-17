import sys
input = sys.stdin.readline

N = int(input())
dp = list(0 for _ in range(N+2))

tp_lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N, 0, -1):
    t, p = tp_lst.pop()
    if i + t <= N + 1:
        dp[i] = max(dp[i+1], dp[i+t]+p)
    else:
        dp[i] = dp[i+1]
        
print(dp[1])