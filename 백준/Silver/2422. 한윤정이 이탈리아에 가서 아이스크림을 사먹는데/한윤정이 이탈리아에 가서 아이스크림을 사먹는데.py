import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ice = [[False for _ in range(N)] for _ in range(N)]
for i in range(M):
    i1, i2 = map(int, input().split())
    ice[i1-1][i2-1] = True
    ice[i2-1][i1-1] = True

result = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if not ice[i][j] and not ice[i][k] and not ice[j][k]:
                result += 1

print(result)