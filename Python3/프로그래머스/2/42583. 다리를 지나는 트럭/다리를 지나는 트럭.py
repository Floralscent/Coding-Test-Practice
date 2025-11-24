from collections import deque
def solution(bridge_length, weight, truck_weights):
    l_l = bridge_length; l_w = weight
    q = deque(truck_weights)
    b = deque()
    w = 0 ; l = 0; time = 0
    
    while q or b:
        time+=1
        #
        if b and b[0][1] == time:
            ext, _ = b.popleft()
            w -= ext
        if q and len(b)<l_l and w+q[0]<=l_w:
            now = q.popleft()
            w += now
            b.append((now,time+l_l))
    
    
    return time