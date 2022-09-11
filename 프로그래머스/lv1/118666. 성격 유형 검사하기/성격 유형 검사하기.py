from collections import defaultdict

def solution(survey, choices):
    dict_a = defaultdict(int)
    n = len(survey)
    
    for i in range(n):
        if choices[i] > 4:          # 동의
            dict_a[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:        # 비동의
            dict_a[survey[i][0]] += 4 - choices[i]
    
    answer = ''
    
    if dict_a['R'] >= dict_a['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dict_a['C'] >= dict_a['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dict_a['J'] >= dict_a['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dict_a['A'] >= dict_a['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer