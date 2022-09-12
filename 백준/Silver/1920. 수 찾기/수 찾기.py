from collections import defaultdict

int_dict = defaultdict(int)
n = int(input())
lst = list(map(int, input().split()))

for i in lst:
    int_dict[i] = 1

m = int(input())
lst_m = list(map(int, input().split()))

for i in lst_m:
    if int_dict[i] != 0:
        print(1)
    else:
        print(0)