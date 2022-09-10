n, k = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)
prize = score[:k]
print(prize[-1])