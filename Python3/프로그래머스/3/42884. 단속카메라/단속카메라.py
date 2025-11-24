def solution(routes):
    routes.sort(key = lambda x : (x[1],x[0]))
    check = -30001
    idx = 0
    
    for i in range(len(routes)):
        if check <routes[i][0]:
            idx +=1
            check = routes[i][1]
    
    return idx