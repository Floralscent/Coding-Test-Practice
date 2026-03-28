import sys
import heapq

input = sys.stdin.readline

n = int(input())

h = []

for _ in range(n):
    tmp = list(map(int, (input().split())))
    #
    for i in range(n):
        if len(h)>=n:
            heapq.heappush(h,tmp[i])
            heapq.heappop(h)
        #
        else:
            heapq.heappush(h, tmp[i])
    #
#
ans = heapq.heappop(h)
print(ans)
        