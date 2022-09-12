from collections import defaultdict

def solution(id_list, report, k):
    s_report = list(set(report))        # 각 유저의 동일한 유저에 대한 신고 횟수는 1회로 처리됨
    
    lst = []                            # report를 공백 기준으로 나눠 리스트로 담아 나타낼 리스트
    for i in range(len(s_report)):
        lst.append(s_report[i].split())
    
    id_report_dict = defaultdict(list)  # 각 유저별로 신고한 아이디를 값으로 저장할 딕셔너리
    id_reported_dict = defaultdict(int) # 각 유저별로 신고당한 횟수를 저장할 딕셔너리
    for i in range(len(s_report)):
        id_report_dict[lst[i][0]].append(lst[i][1])
        id_reported_dict[lst[i][1]] += 1
    
    banned_lst = []
    for key, value in id_reported_dict.items():
        if value >= k:
            banned_lst.append(key)
    
    id_report_success_dict = defaultdict(int)    
    for key, value in id_report_dict.items():
        for i in banned_lst:
            if i in value:
                id_report_success_dict[key] += 1
    
    answer = []
    for i in id_list:
        answer.append(id_report_success_dict[i])
    
    return answer