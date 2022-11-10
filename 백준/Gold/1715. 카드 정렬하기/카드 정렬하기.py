import sys
import heapq

N = int(sys.stdin.readline())
cnt = 0
heap = []

for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

while len(heap) > 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x+y)
    cnt += (x+y)

print(cnt)
