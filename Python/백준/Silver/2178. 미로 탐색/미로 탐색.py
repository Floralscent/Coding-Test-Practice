import sys
from collections import deque

input = sys.stdin.readline

N, M =  map(int, input().rstrip().split())
v = [[0]*M for _ in range(N)]
arr = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs(si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 0
    di = [-1,1,0,0]; dj = [0,0,-1,1]
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci+di[k]; nj = cj+dj[k]
            if(0<=ni<=N-1 and 0<=nj<=M-1 and arr[ni][nj]== 1 and v[ni][nj] == 0):
                q.append((ni,nj)); v[ni][nj] = v[ci][cj]+1

    return v[ei][ej]
ans = bfs(0, 0, N-1, M-1)+1
print(ans)