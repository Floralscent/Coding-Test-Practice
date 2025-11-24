'''
from collections import deque
def solution(people, limit):
    people.sort()
    answer = 0
    q = deque(people)
    
    while q:
        
        if len(q) == 1:
            answer +=1
            break
        #
        if q[0]+q[-1] <= limit:
            q.popleft()
            q.pop()
            answer+=1
        else:
            q.pop()
            answer+=1
    
    return answer
'''

def solution(people, limit):
    people.sort()
    n = len(people)
    visited = [0] * n
    answer = 0
    
    min_idx = 0
    mx_idx = n - 1

    
    while min_idx <= mx_idx:
        
        
        if people[min_idx] + people[mx_idx] <= limit:
            
            answer += 1
            min_idx += 1
            mx_idx -= 1
            
        
        else:
            
            answer += 1
            
            mx_idx -= 1
            
    return answer