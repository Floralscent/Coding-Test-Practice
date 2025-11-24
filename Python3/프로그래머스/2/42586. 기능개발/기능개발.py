import math
from collections import deque

def solution(progresses, speeds):
    n = len(speeds)
    s = deque()
    ans = []
    
    for i in range(n):
        d = math.ceil((100 - progresses[i]) / speeds[i])
        s.append(d)
        

    # 
    mx = s.popleft()
    cnt = 1
    
    # 
    while s:

        if mx >= s[0]:
            s.popleft()
            cnt += 1
        else:
            
            ans.append(cnt)
            mx = s.popleft()
            cnt = 1
            
    ans.append(cnt)
    
    return ans