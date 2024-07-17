M, N = map(int, input().split())

d = {'1': 'o', '2': 'tw', '3': 'th', '4': 'fo', '5': 'fi', '6': 'si', '7': 'se', '8': 'e', '9': 'n', '0': 'z'}

lst = []

for i in range(M, N+1):
    w = ' '.join(d[c] for c in str(i))
    lst.append([i, w])

lst.sort(key=lambda x: x[1])

for i in range(len(lst)):
    if i % 10 == 0 and i != 0:
        print()
    print(lst[i][0], end=' ')