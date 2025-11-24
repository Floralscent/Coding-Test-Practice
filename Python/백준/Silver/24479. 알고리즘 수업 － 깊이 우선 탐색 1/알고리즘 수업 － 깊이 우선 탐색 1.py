import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline
n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)  
order = 1  # 방문 순서 기록할 변수

def dfs(st_node):
    global order
    visited[st_node] = order  
    for i in graph[st_node]:
        if not visited[i]:
            order+=1
            dfs(i)
# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, n+1):
    graph[i].sort()

dfs(r)

for i in range(1, n+1):
    print(visited[i])
