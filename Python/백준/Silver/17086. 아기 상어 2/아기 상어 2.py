#1인 아기상어 기준으로 모든거 방문, 그리고 v는 최솟값으로 갱신
#v중에 최대값 제출

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, (input().split()))
graph = []
li = []
INF = int(1e9)
v = [([INF] * m) for _ in range(n)] 

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] == 1:
            li.append((i, j))
            v[i][j] = 0

def bfs(lst):
    q = deque()
    for i,j in lst:
        q.append((i,j))
    #
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    while q:
        oi,oj = q.popleft()
        for d in range(8):
            ni = oi+dx[d]
            nj = oj+dy[d]
            
            if 0<=ni<n and 0<=nj<m and graph[ni][nj] == 0 and v[ni][nj] == INF:
                q.append((ni,nj))
                v[ni][nj] = v[oi][oj]+1
            #
        #
    #
    return max([max(row) for row in v])
#
ans = bfs(li)
print(ans)
        
