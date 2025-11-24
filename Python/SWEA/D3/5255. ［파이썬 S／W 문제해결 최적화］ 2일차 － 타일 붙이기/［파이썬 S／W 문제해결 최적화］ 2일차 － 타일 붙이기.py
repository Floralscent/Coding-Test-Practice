T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1 ; dp[2] = 3; dp[3]=6
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2]*2+dp[i-3]
        
    #
    print(f"#{test_case} {dp[n]}")