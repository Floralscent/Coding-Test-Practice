def solution(numbers):
    numbers = list(map(str, numbers))
    
    # 커스텀 정렬: 두 숫자를 이어 붙였을 때 더 큰 값이 앞에 오도록 원소는 세자리 숫자까지라 세번 반복
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 0000 같은 경우를 방지
    return str(int(''.join(numbers)))
