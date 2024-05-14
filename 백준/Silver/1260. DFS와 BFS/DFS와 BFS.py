from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

# 정점이 연결된 다른 정점의 번호 기록할 리스트
graph = [[] for _ in range(n+1)]

# 간선 정보 입력
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 정점 방문 여부 기록할 리스트
visited = [False]*(n+1)
# dfs 수행한 결과 저장용 리스트
dfs_ans = list()

# 재귀를 이용한 dfs
def dfs(v):
    visited[v] = True
    dfs_ans.append(v)
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)

dfs(v)

print(*dfs_ans)

# 정점 방문 여부 리셋
visited = [False]*(n+1)
# bfs 수행한 결과 저장용 리스트
bfs_ans = list()

# 데크를 이용한 bfs
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