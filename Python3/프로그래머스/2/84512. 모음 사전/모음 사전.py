from itertools import product

def solution(word):
    # 알파벳 집합
    chars = ['A', 'E', 'I', 'O', 'U']
    
    # 모든 단어를 저장할 리스트
    dictionary = []

    # 1자리부터 5자리까지 중복 순열로 모든 단어를 생성
    for i in range(1, 6):  # 1자리부터 5자리까지
        for w in product(chars, repeat=i):  # chars에서 중복을 허용한 순열 생성
            dictionary.append(''.join(w))  # 튜플을 문자열로 변환해서 리스트에 추가

    dictionary.sort()
    return dictionary.index(word) + 1
