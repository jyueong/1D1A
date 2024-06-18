N = int(input())

num = list()

for _ in range(N):
    num.append(input()[::-1])

ans = 1
cut = set()

while ans < len(num[0]):
    for i in range(N):
        cut.add(num[i][0:ans])
    if len(cut) == len(num):
        break
    else:
        ans += 1
        cut = set()

print(ans)