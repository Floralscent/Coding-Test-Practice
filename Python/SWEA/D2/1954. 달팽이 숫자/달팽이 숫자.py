N = int(input()) # num of test_case

for k in range(1,N+1):
    n = int(input())
    arr = [[0] *n for _ in range(n)]
    dx = [0,1,0,-1] ; dy = [1,0,-1,0]; 
    j = 0 ; x = 0; y = 0
    arr[x][y] = 1 
    for i in range(2,n**2+1):
        nx = x +dx[j%4] 
        ny = y+dy[j%4]
        if 0<= nx<n and 0<=ny<n and arr[nx][ny] == 0:
            x = nx; y = ny
            arr[x][y] = i
        else:
            j+=1
            nx = x +dx[j%4] 
            ny = y+dy[j%4]
            if 0<= nx<n and 0<=ny<n and arr[nx][ny] ==0:
                x = nx; y = ny
                arr[x][y] = i
    print("#"+str(k))
    for r in range(len(arr)):
        print(*arr[r])
       