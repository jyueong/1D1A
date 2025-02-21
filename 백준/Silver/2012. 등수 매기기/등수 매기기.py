N = int(input())
lst = list()
for i in range(N):
    lst.append(int(input()))

lst.sort()

ans = 0

for i in range(1, N+1):
    ans += abs(i-lst[i-1])

print(ans)