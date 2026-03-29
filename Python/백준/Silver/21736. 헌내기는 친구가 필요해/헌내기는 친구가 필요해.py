import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, (input().split()))
graph = []
v = [([0]*m) for _ in range(n)]
t_i = 0; t_j = 0

for i in range(n):
    tmp = list(map(str, (input().strip())))
    if "I" in tmp:
        t_i = i
        t_j = tmp.index("I")
    #
    graph.append(tmp)
#

def bfs(i,j):
    q = deque()
    v[i][j] = 1
    q.append((i,j))
    ans = 0
    dx = [-1,1,0,0]; dy = [0,0,-1,1]
    
    while q:
        oi, oj = q.popleft()
        if graph[oi][oj] == "P":
            ans+=1
        for d in range(4):
            ni = oi+dx[d]
            nj = oj+dy[d]
            
            if 0<=ni<n and 0<=nj<m and graph[ni][nj] !="X" and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = 1
    #
    return ans
##
a = bfs(t_i,t_j)
if a == 0:
    print("TT")
else:
    print(a)