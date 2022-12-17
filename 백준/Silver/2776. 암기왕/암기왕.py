def bi_search(x):
    s = 0
    e = len(lst1) - 1

    while s <= e:
        mid = (s + e) // 2
        if lst1[mid] == x:
            return 1
        elif lst1[mid] < x:
            s = mid + 1
        else:
            e = mid - 1

    return 0


T = int(input())

for t in range(T):
    N = int(input())
    lst1 = sorted(list(map(int, input().split())))
    M = int(input())
    lst2 = list(map(int, input().split()))

    for i in lst2:
        print(bi_search(i))