A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())

ans = 0

for _ in range(3):
    chicken = min(A, X)
    ans += chicken
    A -= chicken
    X -= chicken

    pizza = min(B, Y)
    ans += pizza
    B -= pizza
    Y -= pizza
    
    burger = min(C, Z)
    ans += burger
    C -= burger
    Z -= burger
    
    Y, Z, X = X//3, Y//3, Z//3

print(ans)