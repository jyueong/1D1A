N = int(input())

lst = []

for i in range(N):
    # country, student, score = map(int, input().split())
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: x[2], reverse=True)

for i in range(N):
    if i < 2:
        print(lst[i][0], lst[i][1])
    else:
        if lst[i][0] == lst[0][0] == lst[1][0]:
            pass
        else:
            print(lst[i][0], lst[i][1])
            break