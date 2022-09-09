N = int(input())
cnt = 1
N = N - 1
a = 1
if N != 0:
    while 1:
        # print(int(a*(a+1)/2))
        if N <= int(a*(a+1)/2)*6:
            cnt += a
            break
        else:
            a += 1
    print(cnt)
else:
    print(cnt)