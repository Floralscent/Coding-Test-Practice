from collections import deque

def solution(queue1, queue2):
    #
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    total_sum = sum1 + sum2

    # 애초에 합을 같게 만들 수 없는 경우
    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2
    cnt = 0
    
    # 무한 루프 방지를 위한 탈출 조건 (상한선)
    limit = len(q1) * 4 

    while cnt < limit:
        # 이미 합이 같은 경우
        if sum1 == target:
            return cnt
            
        # q1의 합이 더 크면 q2로 원소 이동
        elif sum1 > target:
            n = q1.popleft()
            q2.append(n)
            sum1 -= n
            sum2 += n
        # q2의 합이 더 크면 q1으로 원소 이동
        else: # sum1 < target
            n = q2.popleft()
            q1.append(n)
            sum1 += n
            sum2 -= n
        
        cnt += 1
        
    # 루프를 다 돌았는데도 답을 못 찾았다면 불가능한 경우
    return -1