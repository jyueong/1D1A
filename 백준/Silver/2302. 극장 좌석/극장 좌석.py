import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
vip = [0] + [int(sys.stdin.readline()) for _ in range(m)]
vip.append(n+1)

dp = [0 for _ in range(41)]
dp[0] = 1
dp[1] = 1
# print(vip)


def makedp(k):
    if dp[k]:
        return dp[k]
    else:
        dp[k] = makedp(k-1) + makedp(k-2)
        return dp[k]


if m == 0:
    print(makedp(n))
else:
    ans = 1
    for i in range(len(vip) - 1):
        ans *= makedp(vip[i+1] - vip[i] - 1)
    print(ans)