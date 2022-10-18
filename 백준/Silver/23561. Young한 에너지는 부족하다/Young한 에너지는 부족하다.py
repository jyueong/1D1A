n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(lst[2*n-1] - lst[n])