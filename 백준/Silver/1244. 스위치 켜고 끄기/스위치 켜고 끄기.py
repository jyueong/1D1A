S = int(input())    # 스위치개수
lst = list(map(int, input().split()))
N = int(input())    # 학생 수

c = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if c[i][0] == 1:            # 남학생이면
        for j in range(S//c[i][1]):
            if lst[c[i][1]-1+c[i][1]*j] == 0:
                lst[c[i][1]-1+c[i][1]*j] = 1
            else:
                lst[c[i][1]-1+c[i][1]*j] = 0

    if c[i][0] == 2:
        if lst[c[i][1]-1] == 0:
            lst[c[i][1]-1] = 1
        else:
            lst[c[i][1]-1] = 0
        m = 1
        while (c[i][1]-1-m >= 0) and (c[i][1]-1+m <= S - 1):
            if lst[c[i][1]-1-m] == lst[c[i][1]-1+m]:
                if lst[c[i][1]-1-m] == 0:
                    lst[c[i][1]-1-m] = 1
                    lst[c[i][1]-1+m] = 1
                else:
                    lst[c[i][1]-1-m] = 0
                    lst[c[i][1]-1+m] = 0
                m += 1
            else:
                break

for i in range(0, S, 20):
    print(*lst[i:i+20])