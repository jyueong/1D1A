n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input())
words = []
for _ in range(m):
    words.append(input())
cnt = 0
for word in words:
    if word in s:
        cnt += 1
print(cnt)