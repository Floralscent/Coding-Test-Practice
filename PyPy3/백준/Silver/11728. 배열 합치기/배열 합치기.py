import sys

input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())  # 첫 줄에서 n과 m을 입력받음
li_n = list(map(int, input().split()))  # 첫 번째 배열 입력받아 정수 리스트로 변환
li_m = list(map(int, input().split()))  # 두 번째 배열 입력받아 정수 리스트로 변환

# 두 리스트 합치기
result = li_n + li_m

# 정렬
result.sort()

print(*result)