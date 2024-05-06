N, M = map(int, input().split())

# M개의 기타줄 브랜드 중 가장 저렴한 패키지 가격, 낱개 가격 저장
p, u = map(int, input().split())
for i in range(M-1):
    canp, canu = map(int, input().split())
    p = min(p, canp)
    u = min(u, canu)

# 낱개 6개 구매 가격이 패키지보다 저렴할 경우 필요한 기타줄 N개 전체를 낱개로 구메
if u*6 <= p:
    print(N*u)

# 패키지가 낱개 6개 구매 가격보다 저렴할 경우
else:
    pn, un = divmod(N, 6)
    print(min(p*(pn+1), p*pn+un*u))