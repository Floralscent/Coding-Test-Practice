import heapq
T = int(input())

def dijstra(i,j):
    q = []
    visited[i][j] = graph[i][j]
    heapq.heappush(q,(graph[i][j],(i,j)))
    while q:
        dist, (x,y) = heapq.heappop(q)
        if dist > visited[x][y]:
            continue
        #
        for i in range(4):
            nx = x +dx[i] ; ny = y +dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost = dist+graph[nx][ny]
                if cost < visited[nx][ny]:
                    visited[nx][ny] = cost
                    heapq.heappush(q,(cost,(nx,ny)))
                    
for test_case in range(1, T + 1):
    # 
    n = int(input())
    graph = [list(map(int, (input()))) for _ in range(n)]
    INF = int(1e9)
    visited = [[INF] * n for _ in range(n)]
    dx = [-1,1,0,0] ; dy = [0,0,-1,1]
    dijstra(0,0)
    print(f"#{test_case} {visited[n-1][n-1]}")