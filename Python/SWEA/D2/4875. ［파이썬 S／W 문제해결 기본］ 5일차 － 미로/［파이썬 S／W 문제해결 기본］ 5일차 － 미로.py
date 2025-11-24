from collections import deque
T = int(input().rstrip())
for test_case in range(1, T + 1):
    #
    n = int(input())
    arr = [list(map(int, (list(input())))) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if 3 in arr[i]:
            ei = i ;  ej = arr[i].index(3)
        if 2 in arr[i]:
            si = i; sj = arr[i].index(2)
    #
    def bfs(si,sj,ei,ej):
        q = deque()
        q.append((si,sj))
        visited[si][sj] = 1
        dx = [-1,1,0,0] ; dy = [0,0,-1,1]
        while q:
            i, j = q.popleft()
            for w in range(4):
                ni = i+dx[w] ; nj = j+dy[w]
                if 0<=ni<n and 0<=nj <n and visited[ni][nj] == 0:
                    if arr[ni][nj] == 0 or arr[ni][nj] == 3: 
                        visited[ni][nj] = visited[i][j] + 1
                        q.append((ni,nj))
                    #
               #
            #
        return visited[ei][ej]
    if bfs(si,sj,ei,ej):
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
        