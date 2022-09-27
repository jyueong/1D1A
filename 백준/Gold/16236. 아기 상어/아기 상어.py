import sys
from collections import deque
from copy import deepcopy

n = int(sys.stdin.readline().rstrip())
lst = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
fish = [0] * 7
shark = 2
time = 0
grow = 0
time_copy = 0

for i in range(n):
    for j in range(n):
        if lst[i][j] == 9:
            x_s, y_s = i, j
            lst[i][j] = 0
        elif lst[i][j]:
            fish[lst[i][j]] += 1

# print(fish)
fish_ori = deepcopy(fish)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

q = deque()
q.append((x_s, y_s, time))

def bfs():
    global time, shark, grow, q, visited, n, x, y, fish_ori
    visited = []
    food = []
    eat = None
    while q:
        x, y, time = q.popleft()
        if 0 < lst[x][y] < shark:
            if not eat:
                eat = time
                food.append((x, y, time))
            elif eat == time:
                food.append((x, y, time))
            else:
                eat = None
                break
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n and lst[x + dx[i]][y + dy[i]] <= shark and (x + dx[i], y + dy[i]) not in visited:
                q.append((x + dx[i], y + dy[i], time + 1))
                visited.append((x + dx[i], y + dy[i]))
    food.sort()
    if food:
        x, y, time = food[0]
        q = deque()
        q.append((x, y, time))
        fish[lst[x][y]] -= 1
        lst[x][y] = 0
        grow += 1
        if grow == shark:
            grow = 0
            shark += 1

while 1:
    if sum(fish[:shark]) == 0:
        break
    lst_before = deepcopy(lst)
    time_copy = time
    bfs()
    if lst_before == lst:
        time = time_copy
        break
    else:
        time_copy = time

print(time_copy)