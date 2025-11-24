'''from itertools import combinations
t = int(input())

def dfs(num, cnt):
    global ans
    if cnt == k:
        ans = max(ans , int(num))
        return
    li = list(num)
    idx = [ i for i in range(len(li))]
    for x,y in combinations(idx , 2):
        li[x], li[y] = li[y], li[x]
        num = "".join(li)
        dfs(num,cnt+1)
        li[x], li[y] = li[y], li[x]

        



for q in rang(1,t+1):
    num, k = input().split()
    k = int(k)
    ans = 0
    dfs(num,0)
    print("#"+str(q), ans)
''' 
from itertools import combinations
t = int(input())


def dfs(num, cnt):
    global ans
    if cnt == k:
        ans = max(ans,int(num))
        return 
    if (num,cnt) in visited:
        return # 가지치기
    visited.add((num,cnt))
    
    li = list(num)
    idx = [i for i in range(len(li))]
    
    for x,y in combinations(idx,2):
        li[x],li[y] = li[y],li[x]
        num = ''.join(li)
        dfs(num, cnt+1)
        li[x],li[y] = li[y],li[x]

for q in range(1,t+1):
    num,k = input().split()
    k = int(k)
    visited = set()
    ans = 0
    dfs(num, 0)
    print("#"+str(q),ans)