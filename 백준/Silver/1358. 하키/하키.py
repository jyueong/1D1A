import math

w, h, x, y, p = map(int, input().split())
cnt = 0

for i in range(p):
    px, py = map(int, input().split())

    if x <= px <= x + w and y <= py <= y + h:
        cnt += 1
    elif math.dist([px, py], [x, y+h//2]) <= h//2:
        cnt += 1
    elif math.dist([px, py], [x+w, y+h//2]) <= h//2:
        cnt += 1

print(cnt)