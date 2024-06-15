import sys

input = sys.stdin.readline

N = int(input())
s_lst = []
e_lst = []

for i in range(N):
    s, e = map(int, input().split())
    s_lst.append(s)
    e_lst.append(e)

ans = max(s_lst) - min(e_lst)

if ans >= 0:
    print(ans)
else:
    print(0)