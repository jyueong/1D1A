N = int(input())

lst = []

for i in range(N):
    x, y = map(int, input().split())
    lst.append([x, y, 0])

for i in range(N):
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            lst[i][2] += 1

for i in range(N):
    print(lst[i][2]+1, end=" ")