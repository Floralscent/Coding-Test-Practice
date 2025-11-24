import sys
sys.setrecursionlimit(10000)
from collections import deque

input = sys.stdin.readline


def dfs(x,y,m,n):
    dx = [0,0,-1,1]; dy = [-1,1,0,0]
    
    v[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 이동할 위치가 배추밭 내에 있는지 확인하고, 방문하지 않은 배추(1)를 찾음
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1 and v[nx][ny] == 0:
            dfs(nx, ny, m, n)
    

t = int(input().strip())
# 테스트 케이스 
for _ in range(t):
    # 그래프 초기화
    m,n,k = map(int, input().rstrip().split())
    graph = [[0]*(n) for _ in range(m)]
    v = [[0]*(n) for _ in range(m)]
    for _ in range(k):
        r, c = map(int, input().rstrip().split())
        graph[r][c] = 1
    # dfs 시작 
    result = 0
    for i in range(m):
        for j in range(n):
             if graph[i][j] == 1 and v[i][j] == 0:  # 배추가 있고 방문하지 않았으면
                dfs(i, j, m, n)
                result += 1  # 새로운 군집이므로 결과값 증가
                
    print(result)
