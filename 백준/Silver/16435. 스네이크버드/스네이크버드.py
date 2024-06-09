N, L = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

for h in lst:
    if L >= h:
        L += 1
    else:
        break

print(L)