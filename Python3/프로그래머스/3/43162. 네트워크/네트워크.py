def solution(n, computers):
    v = [-1]*n
    
    def dfs(i):
        v[i] = 1
        print(i)
        for j in range(n):
            if computers[i][j]==1 and v[j] == -1:
                dfs(j)

    #
    cnt = 0
    for i in range(n):
        if v[i] == -1:
            dfs(i)
            cnt+=1
    
    return cnt