dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < n and info[nx][ny] != 'O':
            if info[nx][ny] == 'S':
                return True
            else:
                nx += dx[i]
                ny += dy[i]
    return False

def obs(cnt):
    global flag
    if cnt == 3:
        for t in t_lst:
            x, y = t[0], t[1]
            if check(x, y):
                break
        else:
            flag = True
    else:
        for i in range(n):
            for j in range(n):
                if info[i][j] == 'X':
                    info[i][j] = 'O'
                    cnt += 1
                    obs(cnt)
                    info[i][j] = 'X'
                    cnt -= 1


n = int(input())
info = [list(input().split()) for _ in range(n)]
t_lst = []
cnt = 0
flag = False

for i in range(n):
    for j in range(n):
        if info[i][j] == 'T':
            t_lst.append((i, j))

obs(0)
if flag:
    print('YES')
else:
    print('NO')