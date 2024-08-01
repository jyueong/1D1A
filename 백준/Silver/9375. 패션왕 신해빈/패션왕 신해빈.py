from collections import defaultdict

T = int(input())

for t in range(T):
    n = int(input())
    clothes = defaultdict(int)
    for i in range(n):
        c1, c2 = input().split()
        clothes[c2] += 1

    if n == 0:
        print(0)

    else:
        ans = 1
        for value in clothes.values():
            ans *= (value+1)
        print(ans - 1)