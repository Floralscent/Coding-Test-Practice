# n,k n개의 집, k개의 대피소
# 1 부터 n개의 집의 x, y좌표 거리는 x좌표의 차+ y좌표의 차
# 대피소를 설치하는 방법중 가장 가까운 대피소와 집 사이의 거리중 가장 큰 값이 가장 작을때의 거리

from itertools import combinations

def mis():
    return map(int, input().split())

N, K = mis()
INF = int(1e9)
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = mis()

def max_dist(comb):
    rst = 0
    for i in range(N):
        min_dist = INF
        for c in comb:
            dist = abs(x[i] - x[c]) + abs(y[i] - y[c])
            min_dist = min(min_dist, dist)
        rst = max(rst, min_dist)
    return rst

ans = INF
for comb in combinations(range(N), K):
    ans = min(ans, max_dist(comb))

print(ans)
