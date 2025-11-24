
def solution(dirs):
    visited = set()  #
    m = [[0] * 10 for _ in range(10)]
    x, y = 5, 5  # 
    dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
    dy = {'U': 1, 'D': -1, 'L': 0, 'R': 0}
    
    answer = 0
    
    for d in dirs:
        nx, ny = x + dx[d], y + dy[d]
        # 격자 범위를 벗어나지 않는 경우만 이동
        if 0 <= nx < 11 and 0 <= ny < 11:
            # 현재 위치 → 이동 위치 경로가 처음 방문된 경우
            if (x, y, nx, ny) not in visited:
                visited.add((x, y, nx, ny))  
                visited.add((nx, ny, x, y))  
                answer += 1 

            # 좌표 갱신
            x, y = nx, ny  

    return answer