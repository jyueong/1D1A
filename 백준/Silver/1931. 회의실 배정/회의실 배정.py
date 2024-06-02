N = int(input())

lst = list()

for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: (x[1], x[0]))

ans = 0
EndTime = 0

for S, E in lst:
    if EndTime <= S:
        ans += 1
        EndTime = E

print(ans)