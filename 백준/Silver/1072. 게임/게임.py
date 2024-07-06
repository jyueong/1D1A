X, Y = map(int, input().split())

Z = Y*100//X
left = 0
right = X
ans = X

if Z >= 99:
    ans = -1
else:
    while left <= right:
        mid = (left+right)//2
        if (Y+mid)*100//(X+mid) > Z:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

print(ans)