T = 10

def dfs(a,b):

    if b == 1:
        return a
    return a* dfs(a,b-1)
    
    
for test_case in range(1, T + 1):
    #
    t = int(input())
    n, m = map(int, (input().split()))
    ans = dfs(n,m)
    print(f"#{t} {ans}")