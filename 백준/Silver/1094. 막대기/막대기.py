X = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]

cnt = 0

for i in stick:
  if X == 0:
    break
  if i <= X:
    X -= i
    cnt += 1

print(cnt)