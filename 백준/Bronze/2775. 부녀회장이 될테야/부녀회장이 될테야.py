def cntppl(k, n, memo):
    if k == 0:
        return n
    if n == 1:
        return 1
    if memo[k][n] != 0:
        return memo[k][n]
    memo[k][n] = cntppl(k, n-1, memo) + cntppl(k-1, n, memo)
    return memo[k][n]

T = int(input())
for t in range(T):
    K = int(input())
    N = int(input())
    memo = [[0]*15 for _ in range(15)]
    for i in range(15):
        memo[0][i] = i+1
        memo[i][0] = 1

    print(cntppl(K, N, memo))