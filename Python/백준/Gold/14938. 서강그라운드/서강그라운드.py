import heapq
n,m,l = map(int,(input().split()))
item = [0]+list(map(int,(input().split())))
INF = int(1e9)
graph = [[] for _ in range(n+1)]

for _ in range(l):
    s,e,c = map(int,(input().split()))
    graph[s].append((c,e))
    graph[e].append((c,s))

#
def dijstra(st_node):
    q = []
    heapq.heappush(q,(0,st_node))
    distance[st_node] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        #
        for weight, next_node in graph[now]:
            cost = weight+distance[now]
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost,next_node))
            
#
ans = 0
for i in range(1,n+1):
    
    distance=[INF]*(n+1)
    dijstra(i)
    mx = 0
    for i in range(1,n+1):
        if distance[i] <= m:
            mx += item[i]

    ans = max(mx, ans)
print(ans)