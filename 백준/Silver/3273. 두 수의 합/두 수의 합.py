import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

lst.sort()

ans = 0

s = 0
e = n-1

while s < e:
    if lst[s] + lst[e] == x:
        ans += 1
        s += 1
    elif lst[s] + lst[e] > x:
        e -= 1
    else:
        s += 1

print(ans)