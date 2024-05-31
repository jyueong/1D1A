lst = list(input().split('-'))

# print(lst)

lst2 = list()

for i in lst:
    lst2.append(sum(map(int, i.split('+'))))

# print(lst2)

ans = 2*lst2[0] - sum(lst2)

print(ans)