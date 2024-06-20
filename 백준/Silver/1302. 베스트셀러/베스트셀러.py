import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().rstrip())
books = defaultdict(int)

for _ in range(N):
    book = input().rstrip()
    books[book] += 1

max_cnt = max(books.values())

ans_lst = [book for book, cnt in books.items() if cnt == max_cnt]
ans_lst.sort()

print(ans_lst[0])
