X = int(input())
a = 1
while 1:
    if X <= a*(a+1)/2:
        if a % 2 == 0:
            f = a
            r = 1
            cha = a*(a + 1)/2 - X
            while cha > 0:
                f -= 1
                r += 1
                cha -= 1
            break
        else:
            f = 1
            r = a
            cha = a*(a + 1)/2 - X
            while cha > 0:
                f += 1
                r -= 1
                cha -= 1
            break
    else:
        a += 1
print(f'{f}/{r}')