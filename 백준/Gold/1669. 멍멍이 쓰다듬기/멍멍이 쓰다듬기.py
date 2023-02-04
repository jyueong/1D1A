# 자라야하는 키 = 멍멍이 - 원숭이
# 첫째 날, 마지막 날은 무조건 1cm 만큼
# 즉 하루에 늘릴 수 있는 키의 양은 중간에 최대치를 찍고 다시 내려와야함
# 0, 1, 2(1+1), 4(1+2+1), 9(1+2+3+2+1), 16(1+2+3+4+3+2+1) 이 기준값이 될듯
# 는 n의 제곱수가 기준값이다...
# 그리고 최대 기준값 + 2일 아님 하루 늘어남

import math

X, Y = map(int, input().split())
gap = Y - X

exc = [0, 1, 2, 3]

if gap in exc:
    print(gap)

else:
    n = math.sqrt(gap)
    # 기준값일 경우
    if n == int(n):
        print(int(2*n - 1))
    else:
        extra = gap - int(n)**2
        if extra > int(n):
            print(int(2*int(n) + 1))
        else:
            print(int(2*int(n)))