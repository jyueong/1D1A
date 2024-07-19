lst = []
for i in range(1, 9):
    lst.append([i, int(input())])

lst.sort(key=lambda x: x[1], reverse=True)

ans = 0
ans_lst = []
for i in range(5):
    ans += lst[i][1]
    ans_lst.append(lst[i][0])

ans_lst.sort()

print(ans)
print(*ans_lst)