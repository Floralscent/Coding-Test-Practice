for q in range(1,11):
    n = int(input())
    li = list(map(int, input().split()))
    for i in range(n):
        near_max = max(li) ; near_min = min(li)
        idx, idx_2=li.index(near_max) , li.index(near_min)
        li[idx]-=1 ; li[idx_2]+=1
    print("#"+str(q), max(li) - min(li))