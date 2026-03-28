import sys

input = sys.stdin.readline

n,m = map(int, (input().split()))

li = dict()

for _ in range(n):
    tmp = input().strip()
    # 암기 조건
    if len(tmp) >m-1:
        if tmp in li:
            li[tmp]+=1
        else:
            li[tmp] = 1
        #
    #
#

ans = sorted(li.keys(), key = lambda x: (-li[x], -len(x),x)) 

for i in ans:
    print(i)