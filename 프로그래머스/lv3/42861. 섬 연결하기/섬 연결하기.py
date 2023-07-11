# 아마도 MST...?

def solution(n, costs):
    answer = 0
    visited = set()    
    
    costs.sort(key = lambda x : x[2])
    
    visited.add(costs[0][0])
    
    while len(visited) != n:
        for idx, cost in enumerate(costs):
            if cost[0] in visited and cost[1] in visited:
                continue
            if cost[0] in visited or cost[1] in visited:
                answer += cost[2]
                visited.add(cost[0])
                visited.add(cost[1])
                costs.pop(idx)
                break
            
    return answer