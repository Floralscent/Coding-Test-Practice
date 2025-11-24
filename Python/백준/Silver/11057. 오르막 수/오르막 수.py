n = int(input())
dp = [[0]*12 for _ in range(n+1)]

dp[1][1:10] = [1]*10

for i in range(2,n+1):
    for j in range(1,11):
        if j == 1:
            dp[i][j] = sum(dp[i-1])
        else:
            dp[i][j] = dp[i][j-1] -dp[i-1][j-1]

# print(dp[n])
print(sum(dp[n])%10007)