t = int(input())
for tc in range(t):
    n, word = input().split()
    ans = ''
    for i in range(len(word)):
        if i == int(n) - 1:
            pass
        else:
            ans += word[i]
    print(ans)