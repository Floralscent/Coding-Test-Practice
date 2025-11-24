import sys

input = sys.stdin.readline

n,limit = map(int, (input().split()))

li_w = [] ; li_v= []
dp = [0] * (limit+1)

for _ in range(n):

    w,v = map(int, (input().split()))
    li_w.append(w)
    li_v.append(v)
    
for i in range(n):
    w = li_w[i] ; v = li_v[i]
    
    for j in range(limit,w-1,-1):
        dp[j] = max(dp[j],dp[j-w]+v)
print(max(dp))