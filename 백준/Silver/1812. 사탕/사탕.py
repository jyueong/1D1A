N = int(input())

S = 0
S_lst = list()
C_lst = list()

for i in range(N):
    candy = int(input())
    S_lst.append(candy)
    if i%2 == 0:
        S += candy
    else:
        S -= candy
    # S += candy*(-1)**i

now = S//2
print(now)

for i in range(N-1):
    now = S_lst[i] - now
    print(now)