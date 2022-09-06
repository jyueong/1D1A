N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
min_cnt = 4

for i in range(N-1):
    cnt = 4
    lst2 = [lst[i], lst[i]+1, lst[i]+2, lst[i]+3, lst[i]+4]
    for j in range(1, 5):
        if lst2[j] in lst:
            cnt -= 1
    if min_cnt > cnt:
        min_cnt = cnt
print(min_cnt)