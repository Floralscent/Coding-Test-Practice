from collections import Counter
def solution(k, tangerine):
    cnt = Counter(tangerine)
    li = [(x,y) for x, y in cnt.items()] # 종류 갯수
    li.sort(key= lambda x : (-x[1], x[0]))
    tmp = 0; idx = 0
    answer = 0
    while tmp< k:
        tmp += li[idx][1]
        idx +=1
        answer+=1
        
    return answer