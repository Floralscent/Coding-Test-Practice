import sys
from collections import deque
input = sys.stdin.readline
n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)  # 방문 순서를 저장할 배열
order = 1  # 방문 순서 기록할 변수

def bfs(st_node):
    global order
    queue = deque([st_node])
    visited[st_node] = order  # 첫 번째 방문 순서
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:  # 방문하지 않은 경우
                order += 1
                visited[i] = order  # 방문 순서 기록
                queue.append(i)

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 큰 번호부터 방문하도록 정렬
for i in range(1, n+1):
    graph[i].sort(reverse = True)

# BFS 실행
bfs(r)

# 방문 순서 출력
for i in range(1, n+1):
    print(visited[i])
