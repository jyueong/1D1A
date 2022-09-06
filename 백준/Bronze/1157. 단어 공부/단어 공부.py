lst = list([0]*26)

word = input()

for i in word:
    if i.islower():
        lst[ord(i)-97] += 1
    else:
        lst[ord(i)-65] += 1

max_cnt = 0
for i in lst:
    if i == max(lst):
        max_cnt += 1

if max_cnt > 1:
    print('?')
else:
    print(chr(lst.index(max(lst))+65))