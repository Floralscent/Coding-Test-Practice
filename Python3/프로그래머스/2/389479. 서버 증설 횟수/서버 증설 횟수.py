from collections import deque


def solution(players, m, k):
    # li: 서버 종료 시점과 수를 기록하는 큐
    li = deque()
    # s: 현재 가동 중인 총 서버 수
    # ans: 총 증설한 서버 수 (정답)
    s = 0
    ans = 0
    
    for i in range(len(players)):
        n = players[i]
        
        while li and li[0][0] == i:
            t, e = li.popleft()
            s -= e
        if n<m:
            continue
        tmp = n // m
        
        if tmp > s:
            cnt = tmp - s
            ans += cnt
            s = tmp
            li.append([i + k, cnt])
            
    answer = ans
    return answer