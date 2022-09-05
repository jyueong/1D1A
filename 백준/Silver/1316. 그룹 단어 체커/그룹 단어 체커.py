def wordcheck(word):
    idx = 0
    while 1:
        l = word.count(word[idx])
        for i in range(idx+1, idx+l):
            if word[i] != word[idx]:
                return 0
        idx = idx+l
        if idx >= len(word):
            return 1

N = int(input())
lst = [input() for _ in range(N)]
# print(lst)

ans = []

for word in lst:
    ans.append(wordcheck(word))

print(sum(ans))