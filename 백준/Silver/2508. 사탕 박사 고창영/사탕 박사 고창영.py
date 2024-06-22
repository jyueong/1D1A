T = int(input())

for t in range(T):
    input()
    r, c = map(int, input().split())
    lst = [list(input()) for _ in range(r)]
    # print(lst)
    ans = 0

    for i in range(r):
        for j in range(c):
            if lst[i][j] == 'o':
                if i-1 >= 0 and lst[i-1][j] == 'v' and i+1 < r and lst[i+1][j] == '^':
                    ans += 1
                    lst[i][j] = lst[i-1][j] = lst[i+1][j] = '.'
                elif j-1 >= 0 and lst[i][j-1] == '>' and j+1 < c and lst[i][j+1] == '<':
                    ans += 1
                    lst[i][j] = lst[i][j-1] = lst[i][j+1] = '.'

    print(ans)