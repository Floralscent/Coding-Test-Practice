import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9)
    
    graph = [[] for _ in range(n + 1)]
    
    distance_s = [INF] * (n + 1)
    distance_a = [INF] * (n + 1)
    distance_b = [INF] * (n + 1)

    for start_node, end_node, cost in fares:
        graph[start_node].append((cost, end_node))
        graph[end_node].append((cost, start_node))

    
    def dijkstra(st_node, mode):
        
        if mode == 's':
            distance = distance_s
        elif mode == 'a':
            distance = distance_a
        else: 
            distance = distance_b
            
        q = []
        heapq.heappush(q, (0, st_node))
        distance[st_node] = 0

        while q:
            dist, now = heapq.heappop(q)

            if dist > distance[now]:
                continue
            
            for weight, next_node in graph[now]:
                cost = distance[now] + weight
                
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))

    
    dijkstra(s, 's')
    dijkstra(a, 'a')
    dijkstra(b, 'b')

    
    min_fare = INF
    for i in range(1, n + 1):
        min_fare = min(min_fare, distance_s[i] + distance_a[i] + distance_b[i])

    return min_fare
    
    '''
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                graph[i][j] = 0
    #
    for st,e,c in fares:
        graph[st][e] = c
        graph[e][st] = c
    #
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    
    min_fare = graph[s][a] + graph[s][b]
    
    
    for k in range(1, n + 1):
        fare_via_k = graph[s][k] + graph[k][a] + graph[k][b]
        min_fare = min(min_fare, fare_via_k)

    return min_fare
    '''