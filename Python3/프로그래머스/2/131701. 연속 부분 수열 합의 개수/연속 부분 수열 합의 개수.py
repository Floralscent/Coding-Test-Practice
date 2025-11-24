def solution(elements):
    li = elements *2
    n = len(elements)
    answer = set()
    for i in range(1,n+1):# 부분 수열의 갯수
        for s in range(n): # 시작지점
            tmp = sum(li[s:s+i])
            if not tmp in answer:
                answer.add(tmp)

    
    return len(answer)