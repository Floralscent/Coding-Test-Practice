n = int(input())  # 빨대의 개수
straws = [int(input()) for _ in range(n)]  # 빨대의 길이들을 입력받음

# 내림차순 정렬
straws.sort(reverse=True)

max_perimeter = -1  # 둘레의 최대값을 저장할 변수, 초기값은 -1로 설정

# 삼각형이 가능한 가장 큰 둘레 찾기
for i in range(n - 2):
    # 삼각형 조건 확인: 가장 긴 빨대가 나머지 두 빨대의 합보다 작아야 함
    if straws[i] < straws[i + 1] + straws[i + 2]:
        perimeter = straws[i] + straws[i + 1] + straws[i + 2]
        max_perimeter = max(max_perimeter, perimeter)  # 더 큰 둘레로 갱신

# 결과 출력: 삼각형을 만들 수 있으면 max_perimeter 출력, 없으면 -1 출력
print(max_perimeter)
