'''

3
5 5 4
3 9 1
3 2 7

'''
import heapq
import sys

idx = 1
while True:
    n = int(input())
    if n == 0:
        exit()
    graph = [list(map(int, input().split())) for _ in range(n)]
    INF =int(1e9)
    visited = [[INF] * n for _ in range(n)]

    dx = [-1,1,0,0]; dy = [0,0,-1,1] # 상하좌우

    def dijstra(st_x,st_y):
        q = []
        visited[st_x][st_y] = graph[st_x][st_y]
        heapq.heappush(q,(graph[st_x][st_y],(st_x, st_y)))

        while q:
            dist, (x, y) = heapq.heappop(q)

            if dist > visited[x][y]:
                continue
            
            for i in range(4):
                nx = x +dx[i]; ny = y+dy[i]

                if 0<=nx<n and 0<=ny<n:
                    cost = dist + graph[nx][ny]
                    if visited[nx][ny] > cost:
                        visited[nx][ny] = cost
                        heapq.heappush(q,(cost,(nx,ny)))

    dijstra(0,0)

    print("Problem",str(idx)+":",visited[n-1][n-1])
    idx+=1