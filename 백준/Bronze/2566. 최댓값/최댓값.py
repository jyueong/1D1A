lst = [list(map(int, input().split())) for _ in range(9)]
max_num = lst[0][0]
max_i = 0
max_j = 0
for i in range(9):
    for j in range(9):
        if max_num < lst[i][j]:
            max_num = lst[i][j]
            max_i = i
            max_j = j
print(max_num)
print(max_i + 1, max_j + 1)