from collections import deque
import sys

input = sys.stdin.readline
# 처음 큐에 넣고, 뽑아봐, 뽑은 애가 조건(0<위치<맥스) 조건(방문 안했)
n, k = map(int, input().rstrip().split())

# 프리로케이션
max_num = 100000  # 최대 범위를 100000으로 설정
visited = [False] * (max_num + 1)
distance = [0] * (max_num + 1)  # 최단 시간 기록
prev = [-1] * (max_num + 1)     # 이전 위치 기록 (경로 추적용)

# 
q = deque()
q.append(n)
visited[n] = True

while q:
    now = q.popleft()
    
    if now == k:
        ans_1 = distance[now]
        break
        
    for next_pos in (now - 1, now + 1, now * 2):
        if 0 <= next_pos <= max_num:
            if not visited[next_pos]:
                q.append(next_pos)
                visited[next_pos] = True
                distance[next_pos] = distance[now] + 1
                prev[next_pos] = now  # 이전 위치 기록

                
path = []
cur = k
while cur != -1:
    path.append(cur)
    cur=prev[cur]

print(ans_1)
print(*path[::-1])

    