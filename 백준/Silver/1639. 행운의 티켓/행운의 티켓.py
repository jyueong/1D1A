S = input()

L = len(S)
N = L//2
ans = 0

while N > 0 and ans == 0:
    for i in range(L-2*N+1):
        if sum(map(int, S[i:i+N])) == sum(map(int, S[i+N:i+(2*N)])):
            ans = 2*N
            break
    N -= 1

print(ans)