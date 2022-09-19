from collections import defaultdict
n = int(input())
lst = []
dict_num = defaultdict(int)
for _ in range(n):
    k = int(input())
    lst.append(k)
    dict_num[k] += 1
print(round(sum(lst)/n))
s_lst = sorted(lst)
print(s_lst[n//2])
max_k = [k for k, v in dict_num.items() if max(dict_num.values()) == v]
max_k.sort()
if len(max_k) == 1:
    print(*max_k)
else:
    print(max_k[1])
print(max(lst)-min(lst))