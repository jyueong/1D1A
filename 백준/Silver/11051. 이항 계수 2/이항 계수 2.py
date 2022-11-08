n, k = map(int, input().split())
num = 1
for i in range(n, n-k, -1):
    num *= i
for i in range(1, k+1):
    num //= i
print(int(num % 10007))