import sys
input = sys.stdin.readline

n = int(input().rstrip())
li = [0]+list(map(int, input().rstrip().split()))
dp = [0]* (n+1)

for i in range(1,n+1):
    mx = 0
    for j in range(0,i):
        if li[i] > li[j]:
            mx = max(mx, dp[j])
    dp[i] = mx +1
    
print(max(dp))

 