N = int(input())
lst = list()

for _ in range(N):
    data = list((input()))
    lst.append(data)

def checkLen():
    max_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if lst[i][j] == lst[i][j+1]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(N-1):
            if lst[j][i] == lst[j+1][i]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1

    return max_cnt

ans = 1

for i in range(N):
    for j in range(N-1):
        if lst[i][j] != lst[i][j+1]:
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
            ans = max(ans, checkLen())
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
        if lst[j][i] != lst[j+1][i]:
            lst[j][i], lst[j+1][i] = lst[j+1][i], lst[j][i]
            ans = max(ans, checkLen())
            lst[j][i], lst[j+1][i] = lst[j+1][i], lst[j][i]

print(ans)