import sys
from copy import deepcopy
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(n)]
v_lst = []
ans = 0

for i in range(n):
    for j in range(m):
        if map_lst[i][j] == 2:
            v_lst.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, aft_lst):
    for di in range(4):
        nx = x + dx[di]
        ny = y + dy[di]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1 and aft_lst[nx][ny] == 0:
            aft_lst[nx][ny] = 2
            dfs(nx, ny, aft_lst)


def wall(cnt):
    global ans
    if cnt == 3:
        aft_lst = deepcopy(map_lst)
        # visited = [[0] * m for _ in range(n)]
        tmp = 0
        for v in v_lst:
            x, y = v[0], v[1]
            dfs(x, y, aft_lst)
        for i in range(n):
            for j in range(m):
                if aft_lst[i][j] == 0:
                    tmp += 1
        ans = max(ans, tmp)
    else:
        for i in range(n):
            for j in range(m):
                if map_lst[i][j] == 0:
                    map_lst[i][j] = 1
                    cnt += 1
                    wall(cnt)
                    map_lst[i][j] = 0
                    cnt -= 1

wall(0)
print(ans)