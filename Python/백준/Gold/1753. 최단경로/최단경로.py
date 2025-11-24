import sys
import heapq

input = sys.stdin.readline

n,m = map(int, input().split())
s = int(input())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

def dijstra(st_node):
    q = []
    distance[st_node] = 0
    heapq.heappush(q,(0,st_node))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        for weight, next_node in graph[now]:
            cost = distance[now]+ weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost, next_node))

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b)) # a에서 b까지 c의 코스트
    
dijstra(s)

for i in range(1,len(distance)):
    d = distance[i]
    if d == INF:
        print("INF")
    else:
        print(d)