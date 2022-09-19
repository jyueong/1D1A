start, end = map(int, input().split())
lst = [0] * (end+1)

for i in range(2, int(end**0.5)+1):     # 2부터 끝까지
    if lst[i] == 0:                     # 숫자가 초기화 되어 있을때
        # 배수가 되려면 적어도 제곱배가 필요
        for j in range(i*i, end+1, i):
            lst[j] = 1

for i in range(start, end + 1):         # 소수만 출력
    if i != 1 and lst[i] == 0:          # 1은 제외
        print(i)