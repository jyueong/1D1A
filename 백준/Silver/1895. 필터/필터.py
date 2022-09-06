r, c = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(r)]
t = int(input())

mid = []

for i in range(r-2):
    for j in range(c-2):
        newlst = []
        for a in range(3):
            for b in range(3):
                newlst.append(lst[i+a][j+b])
        newlst.sort()
        mid.append(newlst.pop(4))
cnt = 0

for i in mid:
    if i >= t:
        cnt += 1

print(cnt)