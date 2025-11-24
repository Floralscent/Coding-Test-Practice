from collections import deque
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]; ny =y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] != "1":
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny))
        
for test_case in range(1, T + 1):
    #
    dx = [-1,1,0,0] ; dy =[0,0,-1,1]
    t = int(input())
    n = 16
    graph = [list((input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    s_i = s_j = e_i = e_j = 0
    for i in range(16):
        for j in range(16):
            if graph[i][j] == "2":
                s_i = i; s_j = j
            elif graph[i][j] == "3":
                e_i = i; e_j = j
            
    bfs(s_i,s_j)
    ans = 1 if visited[e_i][e_j] else 0
    print(f"#{test_case} {ans}")