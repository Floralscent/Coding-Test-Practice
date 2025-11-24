import sys

input = sys.stdin.readline

n = int(input().rstrip())
li = [0]+list(map(int, input().rstrip().split()))
dp = [0]*(n+1)
prev = [-1]*(n+1)


for i in range(1,n+1):
    idx = -1
    mx = 0
    for j in range(i):
        if li[i] > li[j]:
            # mx = max(mx, dp[j])인데 dp[j]가 더 클때 j를 알아야함
            if dp[j] > mx:
                mx = dp[j]
                idx = j

    dp[i] = mx +1
    prev[i] = idx

ans1 = max(dp)
print(ans1)

idx = dp.index(ans1)
ans2 = []

while idx != -1:
    ans2.append(li[idx])
    idx = prev[idx]

ans2.reverse()

print(*ans2)

'''
for i in range(1,n+1):
    mx = 0
    for j in range(i):
        if li[i] > li[j]:
            mx = max(mx, dp[i])
    dp[i] = mx +1


order = max(dp)
print(order)
ans =[]
for i in range(n-1,-1,-1):
    if dp[i] == order:
        ans.append(arr[i])
        order -=1

print(*ans[::-1])
'''