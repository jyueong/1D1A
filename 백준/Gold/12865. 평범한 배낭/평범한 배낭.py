n, k = map(int, input().split())
lst = [0 for _ in range(k+1)]

for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, w-1, -1):
        lst[i] = max(v, lst[i], v + lst[i-w])

print(max(lst))