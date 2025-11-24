from collections import deque
T = 10

def bfs(s):
    global ans
    q = deque()
    q.append((99, s))
    visited[99][s] = 1
    while q:
        x, y = q.popleft()
        if x == 0:
            ans.append(y)
            break
        for i in range(3):  # 좌우상 순서
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                break  # 좌/우/상 중 하나 이동하면 나머지 탐색은 하지 않음

for test_case in range(1, T + 1):
    t = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    n = 100
    idx = graph[99].index(2)
    
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    ans = []
    bfs(idx)
    print(f"#{t} {ans[0]}")
