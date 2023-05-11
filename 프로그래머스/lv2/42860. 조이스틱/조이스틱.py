# A BCDEF GHIJK LM N OP QRSTU VWXYZ
def solution(name):
    l = len(name)
    cnt_lst = []
    std = ord('A')
    nz_p = []
    
    for i in range(l):
        cl = name[i]
        if cl == 'A':
            cnt_lst.append(0)
        elif cl <= 'N':
            cnt_lst.append(ord(cl) - std)
            nz_p.append(i)
        else:
            cnt_lst.append(26 - (ord(cl) - std))
            nz_p.append(i)

    cnt = sum(cnt_lst)
            
    if len(nz_p) == 0:
        return 0
    
    elif len(nz_p) == 1:
        return cnt + min(nz_p[0], l - nz_p[0])
    
    elif len(nz_p) == l:
        return cnt + l-1
        
    elif nz_p[0] == 0:
        min_c = min(nz_p[-1], l-nz_p[1])
        
        for i in range(len(nz_p)-1):
            min_c = min(nz_p[i]*2+(l-nz_p[i+1]), (l-nz_p[i+1])*2+nz_p[i], min_c)
            
        return sum(cnt_lst) + min_c
        
    else:
        min_c = min(nz_p[-1], l-nz_p[0])
    
        for i in range(len(nz_p)-1):
            min_c = min(nz_p[i]*2+(l-nz_p[i+1]), (l-nz_p[i+1])*2+nz_p[i], min_c)
            
        return sum(cnt_lst) + min_c
    
#     cnt = 0
#     idx = 0
    
#     while idx < l:
#         cnt += cnt_lst[idx]
#         cnt_lst[idx] = 0
        
#         if sum(cnt_lst) == 0:
#             break
            
#         # 아직 바꿔야하는 이름이 남아있을 경우
#         else:
#             w = 1
#             while 1:
#                 if idx + w < l and cnt_lst[idx+w] != 0:
#                     idx = idx + w
#                     cnt += w
#                     break
#                 elif idx + w >= l and cnt_lst[idx+w-l] != 0:
#                     idx = idx+w-l
#                     cnt += w
#                     break
#                 elif idx-w >= 0 and cnt_lst[idx-w] != 0:
#                     idx = idx - w
#                     cnt += w
#                     break
#                 elif 0 > idx-w and cnt_lst[l+idx-w] != 0:
#                     idx = l + idx - w
#                     cnt += w
#                     break
#                 else:
#                     w += 1
#     return cnt