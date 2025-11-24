import sys

input = sys.stdin.readline

n = int(input().rstrip())
li = [0]+list(map(int, input().rstrip().split()))
dp = [0]*(n+1)
# prev = [-1]*(n+1)

for i in range(1, n+1):
    mx = 0
    #idx = -1
    for j in range(i):
        if li[i] > li[j]:
            if dp[j] > mx: # mx = max(mx, dp[j])
                mx = dp[j]
                idx = j
    #prev[i] = idx
    dp[i] = mx + li[i]

ans1 = max(dp)
print(ans1)