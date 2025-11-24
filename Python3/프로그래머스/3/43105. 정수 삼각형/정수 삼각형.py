def solution(triangle):
    n = len(triangle)
    dp = [[0] * (len(triangle[i])+2) for i in range(n)] 
    dp[0][1] = int(triangle[0][0])
    for i in range(1,len(triangle)): #내가 1층을빼고했으니 +1이 없어야함
        for j in range(1,len(triangle[i])+1): #내가 1을 만들었으니 마지막까지 돌려면 1을 넣
            dp[i][j] = max(dp[i-1][j-1]+int(triangle[i][j-1]),
                           dp[i-1][j]+int(triangle[i][j-1]))
            
    return max(dp[-1])