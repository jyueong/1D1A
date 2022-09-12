import sys

n = int(sys.stdin.readline().rstrip())
s = set()
for i in range(n):
    s.add(int(sys.stdin.readline().rstrip()))
s = sorted(s)
for i in s:
    print(i)