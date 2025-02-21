# 입력받기
N = int(input())
# 5kg 짜리를 최대한 많이 써야 전체 갯수가 적어짐
q,r = divmod(N, 5)
ans = 0
if r == 0:
    ans = N//5
elif r == 1:
    ans = N//5-1+2
    if N//5 < 1:
        ans = -1
elif r == 2:
    ans = N//5-2+4
    if N//5 < 2:
        ans = -1
elif r == 3:
    ans = N//5+1
elif r == 4:
    ans = N//5-1+3
    if N//5 < 1:
        ans = -1

print(ans)