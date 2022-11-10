N, M, L = map(int, input().split())
lst = list(map(int, input().split()))
lst.append(L)
lst.append(0)
lst.sort()


def check(length):
    cnt = 0
    for i in range(1, N + 2):
        cnt += (lst[i] - lst[i-1] - 1) // length
    return cnt


start = 1
end = L

while start <= end:
    mid = (start + end) // 2
    if check(mid) <= M:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)