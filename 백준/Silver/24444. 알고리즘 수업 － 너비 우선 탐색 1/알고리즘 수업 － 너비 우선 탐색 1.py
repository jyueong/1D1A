import sys
from collections import deque


def bfs(e, r):
    global cnt
    q.append(r)
    visited[r] = cnt
    while q:
        v = q.popleft()
        for node in e[v]:
            if visited[node] == 0:
                cnt += 1
                visited[node] = cnt
                q.append(node)


n, m, r = map(int, sys.stdin.readline().rstrip().split())
nodes = list([] for _ in range(n+1))

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    nodes[u].append(v)
    nodes[v].append(u)

for i in range(n+1):
    nodes[i].sort()

q = deque()
visited = [0]*(n+1)
cnt = 1

bfs(nodes, r)

for i in range(1, n+1):
    print(visited[i])