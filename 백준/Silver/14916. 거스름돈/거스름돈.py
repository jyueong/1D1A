n = int(input())

m = n//5

for i in range(m, -1, -1):
    k = n - 5*m
    l, k = divmod(k, 2)
    if k == 0:
        print(m+l)
        break
    else:
        m -= 1

else:
    print(-1)