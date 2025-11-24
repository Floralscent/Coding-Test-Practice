## FIFO로 넣은거 cacheSize 이상의 값에 대하여  pop 한다음 해당 데이터를 append
def solution(cacheSize, cities):
    answer = 0
    li = []
    
    if cacheSize == 0:
        return len(cities) * 5

    #캐시가 비워져있으면 해당 데이터를 append 하고 실행시간 +5
    #캐시가 차있는데 그게 저장된 데이터가 아니면 +5/ 저장된 데이터였음 +1
    
    for i in cities:
        i = i.lower()
        #if len(li) < cacheSize:
        #    li.append(i)
        #    answer += 5
        #if len(li) >= cacheSize:
        if i in li:
            li.remove(i)
            answer += 1 
            li.append(i)
            
        elif i not in li:
            if len(li) >= cacheSize:
                li.pop(0)
            answer += 5
            li.append(i)
            
    return answer