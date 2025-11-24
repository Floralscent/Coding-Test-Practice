from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff = 0
    answer = []

    # 1. 중복 조합 사용
    # 0~10점 과녁에 n개의 화살을 쏘는 모든 경우의 수
    for combi in combinations_with_replacement(range(11), n):
        # 2. 점수 초기화
        ryan_score, apeach_score = 0, 0
        
        # Counter를 이용해 라이언의 과녁 리스트 생성
        ryan_shots = [0] * 11
        counter = Counter(combi)
        for score, count in counter.items():
            ryan_shots[10 - score] = count # 10점 -> 0번 인덱스

        # 점수 계산 로직...
        for i in range(11):
            if ryan_shots[i] > info[i]:
                ryan_score += (10 - i)
            elif info[i] > 0: # 어피치가 0발 쏘면 점수 못 얻음
                apeach_score += (10 - i)

        # 3. 정답 갱신 로직
        diff = ryan_score - apeach_score
        if diff > max_diff:
            max_diff = diff
            answer = ryan_shots
        elif diff == max_diff and max_diff > 0:
            # 낮은 점수부터 비교하여 answer를 업데이트할지 결정
            for i in range(10, -1, -1):
                if ryan_shots[i] > answer[i]:
                    answer = ryan_shots
                    break
                elif ryan_shots[i] < answer[i]:
                    break
    
    if not answer:
        return [-1]
    return answer