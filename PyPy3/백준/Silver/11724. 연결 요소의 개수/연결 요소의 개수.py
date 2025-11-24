import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 연결 요소 개수 세기
cnt = 0
for i in range(1, n+1):  
    if not visited[i]:  
        bfs(i)
        cnt += 1  

print(cnt)
