def solution(phone_book):
    # 1. 전화번호부를 정렬
    phone_book.sort()
    
    # 2. 인접한 두 전화번호를 비교하여 접두어 관계가 있는지 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False  # 접두어 관계가 있으면 False 반환
    
    # 접두어 관계가 없다면 True 반환
    return True
