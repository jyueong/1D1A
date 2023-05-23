from collections import deque

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        maps[i] = list(maps[i])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and maps[i][j] != 'O':
                cnt = 0
                q = deque()
                q.append((i, j))
                while q:
                    r, c = q.popleft()
                    if maps[r][c] != 'X' and maps[r][c] != 'O':
                        cnt += int(maps[r][c])
                        maps[r][c] = 'O'
                        for d in range(4):
                            nr = r + dr[d]
                            nc = c + dc[d]
                            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] != 'X' and maps[nr][nc] != 'O':
                                q.append((nr, nc))
                answer.append(cnt)
    
    if len(answer) == 0:
        answer.append(-1)
    
    answer.sort()
    
    return answer