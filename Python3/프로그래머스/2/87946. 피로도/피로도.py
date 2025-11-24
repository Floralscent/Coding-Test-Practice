from itertools import permutations

def solution(k, dungeons):
    d = dungeons
    n = len(d); mx = 0
    
    for i in range(1,n+1):
        for p in permutations(d,i):
            hp = k
            li = list(p)
            tmp = 0 
            while li:
                ne, mi = li.pop(0)
                if  hp>= ne:
                    hp -=mi
                    tmp +=1
                #
            #
            mx = max(mx,tmp)
    return mx