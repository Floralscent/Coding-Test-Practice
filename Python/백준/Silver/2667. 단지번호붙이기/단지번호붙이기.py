n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]  # 상하
dy = [0, 0, -1, 1]  # 좌우

def dfs(x, y):
    visited[x][y] = 1  # 방문 처리
    count = 1  # 현재 집도 포함하므로 1부터 시작

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:  
                count += dfs(nx, ny)  # 연결된 모든 집을 세기

    return count

li = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:  # 새로운 단지 발견
            li.append(dfs(i, j))

li.sort()
print(len(li))
for size in li:
    print(size)
