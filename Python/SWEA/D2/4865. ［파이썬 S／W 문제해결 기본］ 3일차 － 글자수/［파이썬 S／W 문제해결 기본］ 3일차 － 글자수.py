from collections import Counter
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #
    str1 = list(input())
    str2 = list(input())
    counter = Counter(str2)
    ans = 0
    for w in str1:
        ans = max(ans, counter[w])
    print(f"#{test_case} {ans}")