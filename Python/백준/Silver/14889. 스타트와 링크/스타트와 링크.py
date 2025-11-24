from itertools import combinations

n = int(input())
graph = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

li = [i for i in range(1, n + 1)]
INF = int(1e9)
ans = INF

for team_a in combinations(li, n // 2):
    team_b = [i for i in li if i not in team_a] # tema_a에 안뽑힌 리스트 만들기

    sum_a = sum(graph[x][y] + graph[y][x] for x, y in combinations(team_a, 2))
    sum_b = sum(graph[x][y] + graph[y][x] for x, y in combinations(team_b, 2))

    ans = min(ans, abs(sum_a - sum_b))

print(ans)
