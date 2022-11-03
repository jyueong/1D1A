import sys
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(n)]
v_lst = []
e_lst = []
ans = 0

for i in range(n):
    for j in range(m):
        if map_lst[i][j] == 2:
            v_lst.append((i, j))
        elif map_lst[i][j] == 0:
            e_lst.append((i, j))

candidates = list(combinations(e_lst, 3))
l = len(candidates)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, lst):
    for di in range(4):
        nx = x + dx[di]
        ny = y + dy[di]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1 and lst[nx][ny] == 0:
            lst[nx][ny] = 2
            dfs(nx, ny, lst)


for i in range(l):
    aft_lst = deepcopy(map_lst)
    tmp = 0
    for a, b in candidates[i]:
        aft_lst[a][b] = 1
    for vx, vy in v_lst:
        dfs(vx, vy, aft_lst)
    for r in range(n):
        for c in range(m):
            if aft_lst[r][c] == 0:
                tmp += 1
    ans = max(ans, tmp)

print(ans)