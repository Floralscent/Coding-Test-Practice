# 모든 사람 최단거리, 다이스트라 말고 플로이드 워샽으로 

import sys

input = sys.stdin.readline
INF = int(1e9)
n,m = map(int, (input().split()))
#n numofnode, m numofline
node = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            node[i][j]=0
#
for _ in range(m):
    s,e = map(int, (input().split()))
    #
    node[s][e] = 1
    node[e][s] = 1
#
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            node[j][k] = min(node[j][k], node[j][i]+node[i][k])

            #
#
ans = INF
for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        tmp +=node[i][j]
        
    #
    if tmp < ans:
        ans = tmp
        idx = i
        
print(idx)