import sys
sys.setrecursionlimit(10**6)

def dfs(r, c):
    global cnt
    cnt += 1
    lst[r][c] = 0

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == 1:
            dfs(nr, nc)


N, M, K = map(int, input().split())

lst = [[0 for _ in range(M)] for _ in range(N)]
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
ans = 0

for _ in range(K):
    r, c = map(int, input().split())
    lst[r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            cnt = 0
            dfs(i, j)
            ans = max(ans, cnt)

print(ans)