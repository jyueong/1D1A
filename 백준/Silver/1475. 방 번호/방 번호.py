N = input()

lst = [0 for _ in range(9)]

for i in N:
    if i == '9':
        lst[6] += 1
    else:
        lst[int(i)] += 1

if lst[6]%2 != 0:
    lst[6] = lst[6] // 2 + 1
else:
    lst[6] = lst[6] // 2

print(max(lst))