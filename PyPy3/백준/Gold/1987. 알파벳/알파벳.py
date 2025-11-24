import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# 상하좌우 이동을 위한 좌표
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# DFS 함수
def dfs(sx, sy, cnt):
    global answer
    answer = max(answer, cnt)  # 최대 이동 거리 갱신

    # 4방향 탐색
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]

        # 범위 체크 및 방문 여부 확인
        if 0 <= nx < r and 0 <= ny < c:
            char_index = ord(graph[nx][ny]) - 65  # 알파벳을 인덱스로 변환 ('A'는 65)
            if alpha[char_index] == 0:  # 방문한 적이 없는 알파벳일 때
                alpha[char_index] = 1   # 방문 처리
                dfs(nx, ny, cnt + 1)    # DFS로 이동
                alpha[char_index] = 0   # 백트래킹: 방문 해제

# 입력 받기
r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

# 알파벳 방문 여부 관리 리스트
alpha = [0] * 26

# 시작 위치 알파벳 방문 처리
alpha[ord(graph[0][0]) - 65] = 1
answer = 0

# DFS 탐색 시작
dfs(0, 0, 1)

# 결과 출력
print(answer)
