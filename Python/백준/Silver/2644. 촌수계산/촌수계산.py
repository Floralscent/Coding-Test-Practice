from collections import deque
n = int(input())
t1, t2 = map(int,input().split())
line_num = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
 
def bfs(st_node,ed_node):
    queue = deque([st_node])
    visited[st_node] = True
    cnt = 0
    
    # 기본 bfs 애서 타겟을 언제까지?
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            # print(node, end = " ")
            if node == ed_node:
                return cnt
            for i in graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        cnt+=1
    return -1


for _ in range(line_num):
    a,b  = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

idx = bfs(t1,t2)
print(idx)