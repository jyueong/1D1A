from collections import deque

def fun1(q):
    q.popleft()

def fun2(q):
    q.append(q.popleft())

def fun3(q):
    q.appendleft(q.pop())


N, M = map(int, input().split())
lst = list(map(int, input().split()))
# print(lst)
q = deque([0] * (N+1))
o = 1
for i in lst:
    for j in range(len(q)):
        if i == j:
            q[j] = o
            o += 1
# print(q)
q.popleft()
cnt = 0
for i in range(1, len(lst) + 1):
    idx = q.index(i)
    if idx != 0:
        if idx <= len(q)//2:
            for _ in range(idx):
                fun2(q)
                cnt += 1
        else:
            for _ in range(len(q)-idx):
                fun3(q)
                cnt += 1
    fun1(q)
print(cnt)