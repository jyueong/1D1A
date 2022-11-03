import sys
sys.setrecursionlimit(10**6)


def post_order(start, end):
    if start > end:
        return

    root = node_lst[start]
    idx = start + 1

    while idx <= end:
        if node_lst[idx] > root:
            break
        idx += 1

    post_order(start+1, idx - 1)

    post_order(idx, end)

    print(root)


node_lst = []

while 1:
    try:
        node = int(sys.stdin.readline())
        node_lst.append(node)
    except:
        break

post_order(0, len(node_lst) - 1)