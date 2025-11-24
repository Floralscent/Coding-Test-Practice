import heapq
import sys

input = sys.stdin.readline
n,m,x = map(int, input().split())

INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

def dijstra(st_node):
    q = []
    distance[st_node] = 0
    heapq.heappush(q,(0,st_node))

    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        for weight, next_node in graph[now]:
            cost = dist + weight # 여기가 틀렸네
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost, next_node))
        
    distance[0]  = 0 
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    
dijstra(x)

li = distance.copy()
# print(li)
half = [s for s in range(1, n + 1) if s != x] 
# print(half)
for k in range(len(half)):
    distance = [INF] * (n+1)
    dijstra(half[k])
    li[half[k]] += distance[x]


print(max(li))

