N = int(input())

lst = list(map(int, input().split()))

lst.sort(reverse=True)

# print(lst)

ans = 0

for i in range(N):
    ans += (i+1)*lst[i]

print(ans)