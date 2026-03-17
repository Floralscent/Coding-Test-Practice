import sys
from collections import deque

input = sys.stdin.readline

I, J = map(int, input().split())
graph = []

ans = [[-1] * J for _ in range(I)]
q = deque()

for i in range(I):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(J):
        if row[j] == 2:      
            q.append((i, j))
            ans[i][j] = 0
        elif row[j] == 0:    
            ans[i][j] = 0

# BFS 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    p_i, p_j = q.popleft()
    for d in range(4):
        n_i = p_i + dx[d]
        n_j = p_j + dy[d]
        
        
        if 0 <= n_i < I and 0 <= n_j < J:
            if ans[n_i][n_j] == -1 and graph[n_i][n_j] == 1:
                ans[n_i][n_j] = ans[p_i][p_j] + 1
                q.append((n_i, n_j))

# 정답 출력
for row in ans:
    print(*(row))