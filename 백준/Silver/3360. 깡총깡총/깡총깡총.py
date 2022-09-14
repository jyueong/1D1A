n = int(input())

n = n + 1  # 몰라 일단 앞에 0 만들어서 하나 늘려
omg, r = divmod(n, 6)

if r == 0:
    ans = omg*(omg+1)*3 - omg
elif r == 1:
    ans = omg*(omg+1)*3 - omg + omg + 1
for i in range(2, 6):
    if r == i:
        ans = omg * (omg + 1) * 3 - omg + i * (omg + 1) - 1
        
print(ans%1000000)