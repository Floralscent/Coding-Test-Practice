from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
max_num = 1000000

distance = [0]*(max_num+1)
visited = [False]*(max_num+1)

q = deque()
q.append(n)

while q:
    now = q.popleft()

    if now == k:
        ans = distance[now]
        break
    next_pos = now*2
    if 0<= next_pos <= max_num and visited[next_pos] == False:
        distance[next_pos] = distance[now]
        q.appendleft(next_pos)
        visited[next_pos] = True
    next_pos = now-1
    if 0<= next_pos <= max_num and visited[next_pos] == False:
        distance[next_pos] = distance[now]+1
        q.append(next_pos)
        visited[next_pos] = True
    next_pos = now+1
    if 0<= next_pos <= max_num and visited[next_pos] == False:
        distance[next_pos] = distance[now]+1
        q.append(next_pos)
        visited[next_pos] = True
print(ans)