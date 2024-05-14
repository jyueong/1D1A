from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(n+1)
dfs_ans = list()

def dfs(v):
    visited[v] = True
    dfs_ans.append(v)
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)

dfs(v)

print(*dfs_ans)

visited = [False]*(n+1)
bfs_ans = list()

def bfs(v):
    dq = deque()
    dq.append(v)
    visited[v] = True
    while dq:
        v = dq.popleft()
        bfs_ans.append(v)
        for i in sorted(graph[v]):
            if not visited[i]:
                dq.append(i)
                visited[i] = 1

bfs(v)

print(*bfs_ans)