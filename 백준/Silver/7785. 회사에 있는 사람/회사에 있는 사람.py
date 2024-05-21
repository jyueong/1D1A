import sys
input = sys.stdin.readline

n = int(input().rstrip())
dic = {}

for i in range(n):
    name, status = input().rstrip().split()
    if status == 'enter':
        dic[name] = status
    else:
        del dic[name]

for key in dict(sorted(dic.items(), reverse=True)).keys():
    print(key)