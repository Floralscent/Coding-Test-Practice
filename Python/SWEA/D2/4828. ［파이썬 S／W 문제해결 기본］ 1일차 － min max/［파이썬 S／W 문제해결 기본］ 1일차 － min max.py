t = int(input())

for q in range(1,t+1):
    n = int(input())
    li = list(map(int, input().split()))
    print("#"+str(q), max(li)-min(li))