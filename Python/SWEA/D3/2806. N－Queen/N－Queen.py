T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    v1 = [0] * N
    v2 = [0] * (2*N-1)
    v3 = [0] *(2*N-1)
    
    def dfs(i):
        global ans
        if i == N:
            ans+=1
            return
        for j in range(N):
            if v1[j] == 0 and v2[i+j] == 0 and v3[i-j]==0:
                v1[j] = v2[i+j] =v3[i-j] =1
                dfs(i+1)
                v1[j] = v2[i+j] =v3[i-j] =0
    ans =0
    dfs(0)
    print(f"#{test_case} {ans}")
                
  