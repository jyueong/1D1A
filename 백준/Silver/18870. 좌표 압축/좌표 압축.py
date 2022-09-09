N = int(input())
lst = list(map(int, input().split()))
lst_s = sorted(set(lst))
dict_lst = {}

for i in range(len(lst_s)):
    dict_lst[f'{lst_s[i]}'] = i


for i in range(len(lst)):
    lst[i] = dict_lst.get(f'{lst[i]}')
print(*lst)