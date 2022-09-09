a, b, v = map(int, input().split())

# 7일이 걸렸으면 6일간 (a - b) 씩 올라가고 마지막날 a만큼 올라감
v = v - a

if v % (a - b):
    cnt = v // (a - b) + 1
else:
    cnt = v // (a - b)

print(cnt + 1)