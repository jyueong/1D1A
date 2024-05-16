import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(c, r):
    lst[c][r] = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < M and 0 <= nc < N and lst[nc][nr] == 1:
            dfs(nc, nr)

T = int(input())

for t in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    lst = [[0 for _ in range(M)] for i in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        lst[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)