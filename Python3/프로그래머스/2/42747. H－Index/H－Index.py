def solution(citations):
    citations.sort() 
    # 오름차선
    # [0,1,3,5,6]
    
    n = len(citations); li=[]
    for i in range(n):
        li.append(min(n-i,citations[i]))

    answer = max(li)
    return answer