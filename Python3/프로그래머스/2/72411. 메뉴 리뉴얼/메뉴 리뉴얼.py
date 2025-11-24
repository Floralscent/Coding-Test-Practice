from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer =[]
    dict = {}
    #menu_counts = Counter()
    for wd in orders:
        n = len(wd)
        for num in course:
            if num <= n:
                for comb in combinations(wd,num):
                    c = sorted(comb)
                    tmp = "".join(c)
                    #
                    if tmp in dict:
                        dict[tmp] +=1
                    else:
                        dict[tmp] = 1
                    #
                    #menu_counts[tmp] +=1
                #
            #
        #
    #
    '''
    한 단어 선택, 그 단어의 길이를 확인해서
    코스 요리 조건 확인
    그 단어에서 코스 요리 조합 되는걸 확인
    대신 그 단어 조합이 AB 와 BA가 생기는걸 방지 위해 집합 넣어서 확인
    집합에 없다면 딕셔너리에 넣음
    딕셔너리 키가 없다면 추가 키가 있다면 값+1
    '''
    for num in course:
        max_cnt = 0
        
        for tmp, cnt in dict.items():
            if len(tmp) == num:
                if cnt > max_cnt:
                    max_cnt = cnt
        
        if max_cnt >= 2:
            # 길이가 course 배열에 num과 동일하고 max_cnt
            for tmp, cnt in dict.items():
                if len(tmp) == num and cnt == max_cnt:
                    answer.append(tmp)

    
    answer.sort()
    
    return answer