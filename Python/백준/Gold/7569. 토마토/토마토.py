import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
# [H][N][M]
graph = []
dh = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0]
dm = [0, 0, 0, 0, 1, -1]


for h in range(H):
    board = []
    for n in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        board.append(row)
    graph.append(board)

def bfs():
    q = deque()
    v = [[[0]*M for _ in range(N)] for _ in range(H)]
    global cnt 
    cnt = 0
    days =1
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m] ==1:
                    q.append((h,n,m))
                    v[h][n][m] = 1
                if graph[h][n][m] ==0:
                    cnt +=1
    if cnt == 0:
        return 0
    
    while q:
        # 현재 큐 사이즈 < 오늘 치
        for _ in range(len(q)):
            ch, cn, cm = q.popleft()

            
            for i in range(6):
                nh, nn, nm = ch + dh[i], cn + dn[i], cm + dm[i]
                if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                    if graph[nh][nn][nm] == 0 and v[nh][nn][nm] == 0:
                        v[nh][nn][nm] = 1
                        graph[nh][nn][nm] = 1
                        cnt -=1
                        q.append((nh, nn, nm))
        
        if q:
            days += 1
    #
    return days

d = bfs()
if cnt == 0:
    if d == 0:
        print(0)
    else:
        print(d-1)
else:
    print(-1)
