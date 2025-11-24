import heapq
def solution(jobs):
    idx = 0 ; cnt = 0 ; time = 0
    w =[]
    n = len(jobs)
    jobs.sort(key = lambda x: x[0])
    
    while idx<n or w:
        while idx<n and jobs[idx][0]<=time:
            heapq.heappush(w,(jobs[idx][1],jobs[idx][0],idx))
            idx+=1
        if w:
            n_t,w_t,num = heapq.heappop(w)
            time += n_t
            cnt += (time-w_t)
        else:
            if idx < n:
                time = jobs[idx][0]
    answer = cnt//n
    return answer