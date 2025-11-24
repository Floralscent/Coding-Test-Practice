import sys

n = int(input())

pap = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    a,b = map(int, input().split())
    
    for i in range(10):
        for j in range(10):
            pap[a+i][b+j] = 1

tmp = 0
for q in range(100):
    tmp += pap[q].count(1)
print(tmp)