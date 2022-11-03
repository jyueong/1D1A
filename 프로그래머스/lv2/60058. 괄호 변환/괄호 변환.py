def uandv(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return p[:i + 1], p[i + 1:]


def check(u):
    lst = []
    for i in u:
        if i == '(':
            lst.append(i)
        else:
            if lst:
                lst.pop()
            else:
                return False
    return True


def solution(p):
    answer = ''
    if not p:
        return answer
    u, v = uandv(p)
    if check(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer
