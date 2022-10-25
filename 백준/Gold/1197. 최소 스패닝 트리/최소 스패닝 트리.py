from collections import defaultdict
import sys
import heapq

v, e = map(int, sys.stdin.readline().rstrip().split())
info = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    info[a].append((c, b))
    info[b].append((c, a))


def prim(node):
    mst = []
    visited = {node}
    candidate = info[node]
    heapq.heapify(candidate)

    while len(visited) < v+1 and candidate:
        c, e = heapq.heappop(candidate)

        if e not in visited:
            visited.add(e)
            mst.append((c, e))

            for route in info[e]:
                if route[1] not in visited:
                    heapq.heappush(candidate, route)

    return sum(map(lambda x:x[0], mst))

print(prim(1))