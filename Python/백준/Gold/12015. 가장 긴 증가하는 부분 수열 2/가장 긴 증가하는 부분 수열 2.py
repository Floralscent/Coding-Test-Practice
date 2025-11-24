import sys
import bisect
input = sys.stdin.readline

n = int(input().rstrip())
li = [0] + list(map(int, input().rstrip().split()))
# dp = [0]*(n+1)
dp = [li[1]]
for i in range(1,n+1):
    if li[i] > dp[-1]:
        dp.append(li[i])
    else:
        idx = bisect.bisect_left(dp, li[i])
        #print(idx)

        dp[idx] = li[i]
        #print(dp)
#print(*dp)

'''
6
20 10 10 30 20 50
기준 
n = 1, li[1] = 20 >> dp.append(20)
n = 2, li[2] = 10 >>
'''
print(len(dp))