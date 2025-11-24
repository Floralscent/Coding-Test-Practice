import sys
import heapq

input = sys.stdin.readline

v,e = map(int,(input().split()))

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

def mst(st_node):
    global ans
    q = []
    heapq.heappush(q,(0,st_node))
    while q:
        cost, now  = heapq.heappop(q)
        if visited[now] == True:
            continue
        visited[now] = True
        ans += cost
        for next_cost, next_node in graph[now]:
            if visited[next_node] == False:
                heapq.heappush(q,(next_cost,next_node))

for _ in range(e):
    a,b,c = map(int, (input().split()))
    graph[a].append((c, b))  # (비용, 노드) 순서로
    graph[b].append((c, a))  # 반대 방향도 추가
#
ans = 0
mst(1)

print(ans)
