c,r = map(int,input().split())
t = int(input())
visited = [[0]*c for _ in range(r)]

if c*r < t:
    print(0)

else:
    x = r-1; y = 0
    dx = [-1,0,1,0]; dy = [0,1,0,-1]
    i = 0 ; idx = 1; visited[x][y] = 1
    while idx < t:
        nx = x+ dx[i%4] ; ny = y+dy[i%4]
        
        if -1<nx<r and -1<ny<c and visited[nx][ny] == 0:
            x = nx; y = ny
            idx +=1
            visited[x][y] = idx
        else:
            i+=1
    print(y+1,r-x)