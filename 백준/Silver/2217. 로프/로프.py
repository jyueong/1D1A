N = int(input())
lst = list()
for _ in range(N):
    lst.append(int(input()))
lst.sort()

answers = list()
for i in lst:
    answers.append(i*N)
    N -= 1
    
print(max(answers))