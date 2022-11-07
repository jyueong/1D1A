lst = [0 for _ in range(31)]
for i in range(28):
    n = int(input())
    lst[n] = n
for i in range(31):
    if lst[i] != i:
        print(i)
