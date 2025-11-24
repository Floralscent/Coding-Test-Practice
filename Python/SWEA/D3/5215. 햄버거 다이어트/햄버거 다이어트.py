'''
def dfs(n, cal, cnt):
    global ans
    # 종료 조건: 모든 아이템을 탐색한 경우
    if n == N:
        ans = max(ans, cnt)
        return
    
    dfs(n + 1, cal, cnt)
    
    if cal + li_cal[n] <= limit:
        dfs(n + 1, cal + li_cal[n], cnt + li_ta[n])
'''
t = int(input())
for i in range(1, t + 1):
    N, limit = map(int, input().split())
    dp = [0] *(limit+1)
    #visited = [0] * N
    li_ta = []
    li_cal = []
    for j in range(N): 
        t, cal = map(int, input().split())
        li_ta.append(t)
        li_cal.append(cal)
    
    for j in range(N):
        t,cal = li_ta[j] , li_cal[j]
        for l in range(limit, cal-1, -1):
            dp[l] = max(dp[l], dp[l-cal]+t)
            
    #ans = 0
    #dfs(0, 0, 0)
    print("#"+str(i), max(dp))


