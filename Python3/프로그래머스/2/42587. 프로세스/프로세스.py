from collections import deque
def solution(priorities, location):
    q = deque()
    for k in range(len(priorities)):
        q.append((priorities[k],k))
    #
    idx = 0
    
    while q:
        pr ,lo = q.popleft()
        t_f = True
        for i, j in q:
            if i>pr:
                t_f = False
        #
        if t_f:
            idx+=1
            if lo == location:
                return(idx)
        #
        else:
            q.append((pr,lo))
            
    