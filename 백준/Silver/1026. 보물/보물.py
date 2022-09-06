N = int(input())

lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

s = 0
lst_a.sort()
lst_b.sort(reverse=True)
for i in range(N):
    s += lst_a[i]*lst_b[i]
print(s)