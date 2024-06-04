N, M = map(int, input().split())

ans = 0

if N == 0:
    print(ans)

else:
    ans += 1
    
    lst = list(map(int, input().split()))

    box = 0

    for book in lst:
        if box + book <= M:
            box += book
        else:
            ans += 1
            box = book
    
    print(ans)