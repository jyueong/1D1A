n = int(input())

n = n + 1  # 몰라 일단 앞에 0 만들어서 하나 늘려
omg, r = divmod(n, 6)

if r == 0:
    ans = omg*(omg+1)*3 - omg
elif r == 1:
    ans = omg*(omg+1)*3 - omg + omg + 1
elif r == 2:
    ans = omg*(omg+1)*3 - omg + 2*(omg + 1) - 1
elif r == 3:
    ans = omg*(omg+1)*3 - omg + 3*(omg + 1) - 1
elif r == 4:
    ans = omg * (omg + 1) * 3 - omg + 4 * (omg + 1) - 1
elif r == 5:
    ans = omg * (omg + 1) * 3 - omg + 5 * (omg + 1) - 1

print(ans%1000000)