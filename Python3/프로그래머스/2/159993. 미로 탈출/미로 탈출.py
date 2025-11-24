from collections import deque

def solution(maps):
    n = len(maps);  m = len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                si = i; sj = j
            elif maps[i][j] == "E":
                ei=i; ej = j
            elif maps[i][j] == "L":
                li =i; lj = j
            #
    
    dx = [-1,1,0,0]; dy = [0,0,-1,1]
    #
    def bfs(i,j,di,dj):
        v = [[-1] *m for _ in range(n)]
        q = deque()
        q.append((i,j))
        
        v[i][j] = 0
        while q:
            i,j = q.popleft()
            
            if i == di and j == dj:
                return v[di][dj] # 다돌았는데 접근 못하면 return이 없네?
            #
            for d in range(4):
                nx = i+dx[d]; ny = j+dy[d]
                
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] != "X":
                    if v[nx][ny] == -1:
                        v[nx][ny] = v[i][j]+1
                        q.append((nx,ny))
        #만약 전부 다 돌아도 목적지를 못가면 return 구조가 None이 되니
        return -1
        
    
    ans1 = bfs(si,sj,li,lj) 
    ans2 = bfs(li,lj,ei,ej)
    
    if ans1 != -1 and ans2 != -1:
        return ans1+ans2
    else:
        return -1