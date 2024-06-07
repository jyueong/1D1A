N = int(input())

S = 0
ans = 0

for i in range(1, N+1):
    S += i
    ans += 1
    
    if S > N:
        ans -= 1
        break
        
print(ans)