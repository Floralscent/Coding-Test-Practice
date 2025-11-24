from collections import deque
graph_num = int(input())
line_num = int(input())


visited = [0] * (graph_num+1)
graph = [[] for _ in range(graph_num+1)]


def dfs(node):
    visited[node] = 1

    for i in graph[node]:
        if not visited[i]:
            dfs(i)
    
for _ in range(line_num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
cnt = visited.count(1)-1 # 자기 자신도 1로 만들었기 때문에 -1
print(cnt)