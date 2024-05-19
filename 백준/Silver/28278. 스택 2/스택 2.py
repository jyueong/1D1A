import sys
input = sys.stdin.readline

N = int(input())

s = []

for _ in range(N):
    c = input().split()
    if c[0] == '1':
        s.append(c[1])
    elif c[0] == '2':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif c[0] == '3':
        print(len(s))
    elif c[0] == '4':
        if s:
            print(0)
        else:
            print(1)
    else:
        if s:
            print(s[-1])
        else:
            print(-1)
