N = int(input())
v1 = [0]*N
v2 = [0]*(2*N)
v3 = [0]*(2*N)

def dfs(i):
    global ans
    if i == N:
        ans +=1
        return 
    
    for j in range(N):# 가로, 세로, 대각선 방문여부
        if v1[j] == v2[i+j] == v3[i-j] ==0:
            v1[j] = v2[i+j] = v3[i-j] = 1
            dfs(i+1)
            v1[j] = v2[i+j] = v3[i-j] = 0

ans = 0            
dfs(0)

print(ans)