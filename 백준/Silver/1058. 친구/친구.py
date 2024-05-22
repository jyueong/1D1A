from copy import deepcopy

N = int(input())

lst = [set() for _ in range(N)]

for i in range(N):
    r = input()
    for j in range(N):
        if r[j] == 'Y':
            lst[i].add(j)

lst2 = deepcopy(lst)

max_cnt = 0

for i in range(N):
    friends = lst[i]
    for friend in friends:
        people = lst[friend]
        for person in people:
            if person != i:
                lst2[i].add(person)
    max_cnt = max(max_cnt, len(lst2[i]))

print(max_cnt)