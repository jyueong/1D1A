N = int(input())
M = int(input())
lst = list(map(int, input().split()))

cnt = 0
while len(lst) > 1:
    a = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == M - a:
            lst.pop(0)
            lst.pop(i-1)
            cnt += 1
            break
    else:
        lst.pop(0)
print(cnt)