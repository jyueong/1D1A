n = int(input())
computers = list([] for _ in range(n+1))

e = int(input())
for _ in range(e):
    s, e = map(int, input().split())
    computers[s].append(e)
    computers[e].append(s)

stack = []
visited = set()

stack.append(1)
visited.add(1)

while stack:
    v = stack[-1]
    for computer in computers[v]:
        if computer not in visited:
            visited.add(computer)
            stack.append(computer)
            break
    else:
        stack.pop()

print(len(visited)-1)