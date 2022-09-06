S = list(map(int, input()))

lst = [S[0]]

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        lst.append(S[i])

ze = 0
on = 0

for a in lst:
    if a == 0:
        ze += 1
    elif a == 1:
        on += 1

print(min(ze, on))