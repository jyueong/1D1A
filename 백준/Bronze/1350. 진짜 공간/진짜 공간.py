n = int(input())
lst = list(map(int, input().split()))
c = int(input())
cnt = 0
for i in lst:
    if i%c:
        cnt += (i//c + 1)
    else:
        cnt += i//c
print(cnt*c)