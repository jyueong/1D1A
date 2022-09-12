N = int(input())
s = set()
for _ in range(N):
    s.add(input())
lst = sorted(s, key=lambda x: (len(x), x))
for i in range(len(lst)):
    print(lst[i])