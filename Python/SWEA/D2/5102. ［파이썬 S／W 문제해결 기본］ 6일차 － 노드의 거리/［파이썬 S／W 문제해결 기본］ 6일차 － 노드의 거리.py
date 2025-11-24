from collections import deque
T = int(input())

def chk(s,g):
    q = deque()
    q.append(s)
    
    visited[s] = 1
    
    while q:
        for _ in range(len(q)):
            n = q.popleft()
            for next_node in graph[n]:
                    if visited[next_node] == 0:
                        visited[next_node] =visited[n]+1
                        q.append(next_node)

for test_case in range(1, T + 1):
    #
    v, e = map(int, (input().split()))
    visited = [0] * (v+1)
    graph = [[] for _ in range(v+1)]
    
    for _ in range(e):
        a,b = map(int, (input().split()))
        graph[a].append(b)
        graph[b].append(a)
        # 그래프 셋팅
    #
    s,g = map(int, (input().split()))
    
    chk(s,g)
    ans = visited[g] - 1 if visited[g] >0 else 0
    print(f"#{test_case} {ans}")