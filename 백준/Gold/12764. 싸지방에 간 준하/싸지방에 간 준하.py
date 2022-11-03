import sys
import heapq

n = int(sys.stdin.readline())

heap = []
computers = [0 for _ in range(n)]
count = [0 for _ in range(n)]
use = 0

for i in range(n):
    p, q = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (p, q))

while heap:
    tmp = heapq.heappop(heap)
    for i in range(n):
        if computers[i] <= tmp[0]:
            if computers[i] == 0:
                use += 1
            computers[i] = tmp[1]
            count[i] += 1
            break

print(use)
print(*count[:use])