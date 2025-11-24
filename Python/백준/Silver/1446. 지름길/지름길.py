'''
n,k = map(int,(input().split()))
dp = [j for j in range(10001)]
li =[]
for _ in range(n):
    a,b,c = map(int,(input().split()))
    li.append([a,b,c])
#

for i in range(1,10001):
    dp[i] = min(dp[i],dp[i-1]+1)
    
    for s,e,c in li:
        if e == i:
            dp[e] = min(dp[e],dp[s]+c)
    #
#
print(dp[k])
'''

import heapq
import sys
input = sys.stdin.readline

n,k = map(int,(input().split()))
INF = int(1e9)
distance = [INF]*10001
graph = [[] for _ in range(10001)]

for i in range(10000):
    #
    graph[i].append((1,i+1))# 출발지, 코스트 1, 다음 목적지

#
for j in range(n):
    s,e,c = map(int,(input().split()))
    graph[s].append((c,e))
#

def dijstra(st_node):
    q = []
    heapq.heappush(q,(0,st_node))
    distance[st_node] = 0
    while q:
        dist,now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        #
        for weight,next_node in graph[now]:
            cost = weight + distance[now]
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost,next_node))

dijstra(0)

print(distance[k])





