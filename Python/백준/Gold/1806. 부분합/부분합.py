import sys
n , s =  map(int, input().split())

data = list(map(int,(input().split())))
sm = 0 ; cnt = []; end = 0

for start in range(n):
    while sm < s and end < n:
        sm += data[end]
        end +=1 
    if sm >= s:
        cnt.append(end - start)
    sm -= data[start]
if not cnt:
    print(0)
    exit()
print(min(cnt))