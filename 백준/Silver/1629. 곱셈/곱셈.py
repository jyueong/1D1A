def solve(a, b, c):
    if b == 1:
        return a%c
    else:
        r = solve(a, b//2, c)
        if b%2 == 0:
            return ((r*r)%c)
        else:
            return ((r*r*a)%c)

A, B, C = map(int, input().split())

ans = solve(A, B, C)
print(ans)