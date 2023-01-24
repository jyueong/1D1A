import sys
input = sys.stdin.readline

n, k = map(int, input().split())
info = list(map(int, input().split()))

diff = []
for i in range(1, n):
    diff.append(info[i] - info[i-1])

diff.sort(reverse=True)
print(sum(diff[k-1:]))