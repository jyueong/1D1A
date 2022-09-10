import sys

n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lst.sort(key=lambda x:(x[0], x[1]))
for i in range(n):
    print(*lst[i])