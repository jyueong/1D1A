import sys
sys.setrecursionlimit(10**6)


def dfs(e, r):
    global cnt
    cnt += 1
    visited[r] = cnt
    for node in e[r]:
        if visited[node] == 0:
            dfs(e, node)


n, m, r = map(int, sys.stdin.readline().rstrip().split())
e = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    e[u].append(v)
    e[v].append(u)

for i in range(n+1):
    e[i].sort()

dfs(e, r)

for i in range(1, n+1):
    print(visited[i])