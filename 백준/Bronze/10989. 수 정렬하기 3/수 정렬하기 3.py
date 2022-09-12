import sys
from collections import defaultdict

N = int(sys.stdin.readline())
int_dict = defaultdict(int)
for _ in range(N):
    int_dict[sys.stdin.readline().rstrip()] += 1
# print(int_dict)
for i in range(10001):
    if int_dict[f'{i}'] != 0:
        for j in range(int_dict[f'{i}']):
            print(i)