import heapq
def solution(operations):
    li = []
    for i in operations:
        op,num = i.split()
        li.append([op,int(num)])
    #
    q = []
    for op,num in li:
        if op == "I":
            heapq.heappush(q,num)
        else:
            if q:
                if num == 1:
                    #print(f"D 1 : {max(q)}")
                    q.remove(max(q))
                else:
                    heapq.heappop(q)
            else:
                continue
    #
    if q:
        return [max(q), q[0]]
    else:
        return [0,0]
                    
  