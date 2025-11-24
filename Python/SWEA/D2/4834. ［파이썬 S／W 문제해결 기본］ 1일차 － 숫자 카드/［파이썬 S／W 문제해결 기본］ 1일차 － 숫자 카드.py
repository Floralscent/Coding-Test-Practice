t = int(input())

for q in range(1, t+1):
    n = int(input())
    li = [0]*10
    num = list(input())
    
    for i in num:
        li[int(i)] += 1
        
    max_num =0; idx = 0
    for j in range(10):
        if li[j] >=max_num:
            max_num = li[j]
            idx = j
        
    print("#"+str(q), idx, max_num)