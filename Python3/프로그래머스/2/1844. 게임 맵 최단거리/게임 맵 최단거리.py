from collections import deque
def solution(maps):
    n = len(maps) ; m = len(maps[0])
    v = [[-1]*m for _ in range(n)]
    
    dx = [0,0,1,-1] ; dy = [1,-1,0,0]
    
    def bfs(i,j):
        q = deque()
        q.append((i,j))
        v[i][j] = 1
        
        while q:
            x, y = q.popleft()
            
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if 0<= nx < n and 0<= ny <m:
                    if maps[nx][ny] == 1:
                        if v[nx][ny] == -1:
                            v[nx][ny] = v[x][y]+1
                            q.append((nx,ny))
                            
    
    
    bfs(0,0)
    answer = v[n-1][m-1]
    return answer