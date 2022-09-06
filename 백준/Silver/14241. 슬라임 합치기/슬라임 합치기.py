n = int(input())
lst = list(map(int, input().split()))

lst.sort()
score = 0
while len(lst) >= 2:
    m1 = lst.pop()
    m2 = lst.pop()
    lst.append(m1+m2)
    score += m1*m2

print(score)