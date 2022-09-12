import math

def solution(n, k):
    aft = ''
    while n != 0:
        n, mod = divmod(n, k)
        aft = str(mod) + aft
    lst = aft.split('0')
    num_lst = []
    for i in lst:
        if i != '':
            num_lst.append(int(i))
    cnt = 0
    for i in num_lst:
        if i != 1:
            new_lst = []
            for j in range(2, int(math.sqrt(i) + 1)):
                if i%j == 0:
                    break
            else:
                cnt += 1
    answer = cnt
    return answer