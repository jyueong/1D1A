import sys
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    global size
    painting[r][c] = 2
    size += 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and painting[nr][nc] == 1:
            dfs(nr, nc)


n, m = map(int, input().split())
painting = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
size_lst = [0]

for i in range(n):
    for j in range(m):
        if painting[i][j] == 1:
            size = 0
            dfs(i, j)
            cnt += 1
            size_lst.append(size)

print(cnt)
print(max(size_lst))