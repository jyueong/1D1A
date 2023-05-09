# brown + yellow 의 약수??여야함...?
# brown 10, yellow 2 라면 12니까 세로가 2일때부터 체크
# 2, 6 근데 이러면 노랑이 없네 노랑 있으려면 최소가 3, 3 이니까 세로 3일때부터 체크
# 3, 4 이러면 4*2, 3*2 - 4 = 8 + 6 - 4 = 10 brown 색만 체크하면 될듯?
# 4, 3 도 체크해야하지만 가로가 세로보다 길어지지 않음 뭐 이런식...

def solution(brown, yellow):
    # answer = []
    total = brown + yellow
    height = 3
    width = total / height
    
    while width >= height:
        if int(height) == height:
            if brown == (width*2) + (height*2) - 4:
                return [width, height]
            else:
                height += 1
                width = total / height

        else:
            height += 1
            width = total / height
            
    # return answer