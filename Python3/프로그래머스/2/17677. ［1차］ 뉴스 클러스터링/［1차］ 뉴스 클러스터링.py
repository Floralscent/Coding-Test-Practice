from collections import Counter

def solution(str1, str2):
    # 1단계: 각 문자열을 두 글자씩 잘라 다중 집합(리스트) 만들기
    list_a = []
    for i in range(len(str1) - 1):
        chunk = str1[i:i+2]
        # 영문자로만 구성된 경우만 소문자로 바꿔 추가
        if chunk.isalpha():
            list_a.append(chunk.lower())

    list_b = []
    for i in range(len(str2) - 1):
        chunk = str2[i:i+2]
        if chunk.isalpha():
            list_b.append(chunk.lower())

    # 2단계: Counter를 이용해 교집합과 합집합의 크기 구하기
    # 두 집합이 모두 공집합인 경우, 유사도는 1
    if not list_a and not list_b:
        return 65536

    counter_a = Counter(list_a)
    counter_b = Counter(list_b)

    # Counter의 '&'와 '|' 연산으로 교집합과 합집합 Counter를 생성
    # .values()로 각 원소의 개수를 가져오고, sum()으로 총개수를 계산
    intersection_size = sum((counter_a & counter_b).values())
    union_size = sum((counter_a | counter_b).values())

    # 3단계: 자카드 유사도 계산 후 최종 값 반환
    # 합집합이 0인 경우는 위에서 처리했으므로 0으로 나누는 경우는 없음
    jaccard_similarity = intersection_size / union_size
    
    return int(jaccard_similarity * 65536)