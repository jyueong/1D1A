lst = list(map(int, input().split()))
s = 0
for i in lst:
    s += i**2
print(s%10)