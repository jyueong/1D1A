chess = [list(input()) for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if chess[i][j] == 'F':
            if (i+j)%2:
                pass
            else:
                cnt += 1
print(cnt)