T = int(input())

def dfs(depth,total):
    global ans
    if depth ==n :
        ans = min(total, ans)
        return
    if total >= ans:
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, total + li[depth][i])
            visited[i] = 0



for test_case in range(1, T + 1):
    #
    n = int(input())
    li = [list(map(int, (input().split()))) for _ in range(n)]
    visited = [0] * n
    ans = 11*n
    
    dfs(0,0)
    #
    print(f"#{test_case} {ans}")