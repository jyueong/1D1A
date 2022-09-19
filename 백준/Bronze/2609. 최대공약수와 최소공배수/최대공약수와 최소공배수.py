m, n = map(int, input().split())
a = m
b = n
if b > a:
    a, b = b, a
while b > 0:
    a, b = b, a % b
res1 = a
res2 = int(m*n/res1)
print(res1)
print(res2)