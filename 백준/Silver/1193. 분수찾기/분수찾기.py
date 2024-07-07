X = int(input())

cnt = 1
right = 1
left = 1
flag = True

while cnt != X:
    cnt += right
    right += 1
    if cnt > X:
        cnt -= (right - 1)
        right -= 1
        break
    # cnt: 1 2 4 7
    # right: 1 2 3 4

if right % 2 == 1:
    flag = False

while cnt != X:
    cnt += 1
    right -= 1
    left += 1

if flag == False:
    print(f"{right}/{left}")
else:
    print(f"{left}/{right}")