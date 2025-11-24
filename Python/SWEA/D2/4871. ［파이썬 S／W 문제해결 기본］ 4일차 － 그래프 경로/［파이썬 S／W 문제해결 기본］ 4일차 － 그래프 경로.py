T = int(input())
for test_case in range(1, T + 1):
    # 
    v, e = map(int, (input().split()))
    graph = [[] for  _ in range(v+1)] ; visited = [0] * (v+1)
    for _ in range(e):
        a,b = map(int, (input().split()))
        graph[a].append(b)
        
    s,g = map(int, (input().split()))
    
    def check(a,b):
        visited[a] = 1
        for near in graph[a]:
            if visited[near] == 0:
                check(near,b)
            #
        
        #
    #
    check(s,g)
    ans = visited[g]
    print(f"#{test_case} {ans}")