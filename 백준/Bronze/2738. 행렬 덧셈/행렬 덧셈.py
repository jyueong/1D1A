n, m = map(int, input().split())
lst1 = []
lst2 = []
for i in range(n):
    lst1.append(list(map(int, input().split())))
for i in range(n):
    lst2.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        lst1[i][j] += lst2[i][j]
    print(*lst1[i])