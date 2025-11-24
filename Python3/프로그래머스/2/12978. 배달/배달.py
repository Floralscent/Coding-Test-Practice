import heapq


def solution(N, road, K):
    graph = [[] for _ in range(N+1)] # 0 생략
    INF = int(1e9)
    distance = [INF] * (N+1)
    for s,e,c in road:
        graph[s].append((c,e))
        graph[e].append((c,s))
    #
    def dijstra(st_node):

        q = []
        heapq.heappush(q,(0,st_node))
        distance[st_node] = 0

        while q:
            dist,now = heapq.heappop(q)

            if dist > distance[now]:
                continue
            for weight, next_node in graph[now]:
                cost = distance[now]+weight
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q,(cost,next_node))
    #
    dijstra(1)
    cnt = 0 
    for i in range(1,N+1):
        if distance[i] <=K:
            cnt+=1
    return cnt