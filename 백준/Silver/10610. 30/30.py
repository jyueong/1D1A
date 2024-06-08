N = input()

if '0' not in N:
    print(-1)

else:
    S = 0
    for i in N:
        S += int(i)
    if S%3 != 0:
        print(-1)
    else:
        N = sorted(N, reverse=True)
        for i in N:
            print(i, end="")