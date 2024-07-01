N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0
max_lst = list()

for i in range(N):
    classmate = set()
    for j in range(5):
        for k in range(N):
            if lst[i][j] == lst[k][j]:
                classmate.add(k)
    cnt = len(classmate)
    if max_cnt == cnt:
        max_lst.append(i)
    elif max_cnt < cnt:
        max_lst = [i]
        max_cnt = cnt
    else:
        pass

print(max_lst[0]+1)