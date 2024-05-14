from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0]*(n+1)
ans = list()

def dfs(v):
    visited[v] = 1
    ans.append(v)
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

dfs(v)

print(*ans)

visited2 = [0]*(n+1)
ans2 = list()

def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = 1
    while q:
        v = q.popleft()
        ans2.append(v)
        for i in range(1, n+1):
            if visited2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited2[i] = 1

bfs(v)

print(*ans2)