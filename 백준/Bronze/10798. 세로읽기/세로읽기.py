lst = []
for i in range(5):
    lst.append(input())

ans = ''

for i in range(15):
    for j in range(5):
        try:
            ans += lst[j][i]
        except:
            pass

print(ans)