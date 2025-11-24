import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
distance = [INF] *(n+1)
graph = [[] for _ in range(n+1)]

def dijkstra(st_node):
    q = []
    distance[st_node] = 0
    heapq.heappush(q,(0,st_node))
    
    while q:
        dist,now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        for weight, next_node in graph[now]:
            cost = weight + distance[now]
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost, next_node))

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    # graph[b].append((c,a))

s,d = map(int, input().split())
dijkstra(s)
print(distance[d])