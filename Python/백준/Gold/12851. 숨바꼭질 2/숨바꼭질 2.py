from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

max_num = 100000  # 최대 범위를 100000으로 설정
visited = [False] * (max_num + 1)
distance = [0] * (max_num + 1)  # 최단 시간 기록
prev = [-1] * (max_num + 1)     # 이전 위치 기록 (경로 추적용)
ways = [0] * (max_num + 1)      # 해당 위치까지 도달하는 경로 수

q = deque()
q.append(n)
visited[n] = True  # 초기값
ways[n] = 1        # 시작 위치에서의 경로 수는 1

while q:
    now = q.popleft()
    
    if now == k:
        print(distance[now])
        print(ways[k])
        break
    for next_pos in (now*2, now-1, now+1):
        if 0<= next_pos <= max_num :
            if not visited[next_pos]:
                q.append(next_pos)
                visited[next_pos] = True
                distance[next_pos] = distance[now]+1
                prev[next_pos] = prev[now]
                ways[next_pos] = ways[now]
            elif distance[next_pos] == distance[now]+1:
                    ways[next_pos] += ways[now]                
            
    