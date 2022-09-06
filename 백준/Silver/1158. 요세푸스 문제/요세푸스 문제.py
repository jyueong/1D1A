N, K = map(int, input().split())
lst = list(range(1, N+1))
# print(lst)
res = []
idx = 0
# 시작점

while lst:
    idx = (idx + K - 1) % len(lst)
    res.append(str(lst.pop(idx)))

print('<', ', '.join(res), '>', sep='')