def solution(targets):
    targets.sort(key =  lambda x :  (x[1],x[0]))
    check  = -1
    answer = 0
    
    for i in range(len(targets)):
        if check <= targets[i][0]:
            check = targets[i][1]
            answer+=1
    return answer