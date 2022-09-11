from collections import defaultdict

int_dict = defaultdict(int)

a = int(input())
b = int(input())
c = int(input())
new = str(a*b*c)

for i in new:
    int_dict[i] += 1

for i in range(10):
    print(int_dict[f'{i}'])