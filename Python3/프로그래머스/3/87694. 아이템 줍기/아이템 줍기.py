from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 최대치가 51이었으나 스케일링을 위해 두배
    board = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0 # 내부 공간은 0으로
                elif board[i][j] != 0:
                    board[i][j] = 1 # 테두리는 1로

    # --- 2단계: 2배율 좌표에서 BFS로 최단 거리 찾기 ---
    
    # BFS를 위한 방향 벡터와 큐
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()

    # 캐릭터와 아이템의 좌표도 2배로
    cx, cy = characterX * 2, characterY * 2
    ix, iy = itemX * 2, itemY * 2
    
    # 시작점을 큐에 추가하고, 거리를 기록 (방문 처리)
    q.append([cx, cy])
    visited = [[1] * 102 for _ in range(102)] # 거리 계산용 배열

    while q:
        x, y = q.popleft()
        
        # 목표 지점에 도달하면 현재까지의 거리를 반환
        if x == ix and y == iy:
            # 2배율로 계산된 거리이므로 2로 나눠서 최종 결과 도출
            return visited[x][y] // 2

        # 상하좌우 네 방향으로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어나지 않고, 테두리(1)이면서, 아직 방문하지 않았다면
            if board[nx][ny] == 1 and visited[nx][ny] == 1:
                # 다음 위치의 거리는 현재 위치 거리 + 1
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                
    return 0 # 이론상 도달할 일 없음