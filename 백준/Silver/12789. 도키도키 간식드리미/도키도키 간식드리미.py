N = int(input())
lst = list(map(int, input().split()))

# print(lst)

stack = list()

now_num = 1

for num in lst:
    if num == now_num:
        now_num += 1
        while stack:
            if stack[-1] == now_num:
                stack.pop()
                now_num += 1
            else:
                break
    else:
        if stack:
            if stack[-1] > num:
                stack.append(num)
            else:
                print("Sad")
                break
        else:
            stack.append(num)
else:
    print("Nice")