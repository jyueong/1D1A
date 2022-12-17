def dfs(r, c):
    if wrd[r][c] == '-':
        wrd[r][c] = 'x'

        for dc in [1, -1]:
            nc = c + dc
            if 0 <= nc < m and wrd[r][nc] == '-':
                dfs(r, nc)

    if wrd[r][c] == '|':
        wrd[r][c] = 'x'

        for dr in [1, -1]:
            nr = r + dr
            if 0 <= nr < n and wrd[nr][c] == '|':
                dfs(nr, c)


n, m = map(int, input().split())

wrd = [list(input()) for _ in range(n)]
# print(wrd)
cnt = 0

for i in range(n):
    for j in range(m):
        if wrd[i][j] == '-' or wrd[i][j] == '|':
            dfs(i, j)
            cnt += 1

print(cnt)