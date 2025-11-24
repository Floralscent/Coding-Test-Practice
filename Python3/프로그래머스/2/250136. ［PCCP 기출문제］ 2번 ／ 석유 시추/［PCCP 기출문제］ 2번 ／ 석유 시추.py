from collections import deque

def solution(land):
    n,m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    
    
    oil_info = {}
    oil_id = 2  # (0은 빈 땅, 1은 미탐사 석유)
    dx = [-1,1,0,0]; dy = [0,0,-1,1]
    
    for r in range(n):
        for c in range(m):
            
            if land[r][c] == 1 and not visited[r][c]:
                
                q = deque([(r, c)])
                visited[r][c] = True
                land[r][c] = oil_id
                current_size = 1
                
                while q:
                    i, j = q.popleft()
                    
                    for d in range(4):
                        nx = i+dx[d]; ny=j+dy[d]
                        
                        if 0 <= nx <n  and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            land[nx][ny] = oil_id 
                            current_size += 1
                            q.append((nx, ny))
                
                
                oil_info[oil_id] = current_size
                oil_id += 1 

    
    max_oil = 0
    for c in range(m):
        current_column_oil = 0
        
        seen_ids = set()
        
        for r in range(n):
            if land[r][c] > 1 and land[r][c] not in seen_ids:
                oil_mass_id = land[r][c]
                seen_ids.add(oil_mass_id)
                current_column_oil += oil_info[oil_mass_id]
        
        max_oil = max(max_oil, current_column_oil)
        
    return max_oil