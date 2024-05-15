from collections import deque

n, m = map(int, input().split())
lst = list()
for _ in range(n):
    lst.append(list(input()))

v_lst = [[False for _ in range(m)] for i in range(n)]
d_lst = [[1 for _ in range(m)] for i in range(n)]

# print(lst)

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not v_lst[nx][ny] and lst[nx][ny] == '1':
                    v_lst[nx][ny] = True
                    q.append((nx, ny))
                    d_lst[nx][ny] += d_lst[x][y]

bfs()

print(d_lst[n-1][m-1])