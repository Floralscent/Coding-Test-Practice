from collections import defaultdict,deque
def solution(begin, target, words):
    if not target in words:
        return 0
    #
    
    def chk(wd1,wd2):
        cnt = 0
        wd_li1 = [x for x in wd1]
        wd_li2 = [x for x in wd2]
        for k in range(len(wd_li1)):
            if wd_li1[k] != wd_li2[k]:
                cnt+=1
            if cnt >=2:
                break
            #
        if cnt == 1:
            return True
        else:
            return False
            
                
    #
    
    li = [begin]+words
    n = len(li)
    
    graph = defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            #
            if chk(li[i],li[j]):
                graph[li[i]].append(li[j])
                graph[li[j]].append(li[i])
            #
    ##
    #
    q = deque()
    q.append(begin)
    visited = {begin:0}
    while q:
        now = q.popleft()
        
        if now == target:
            return visited[now]
        
        for next_node in graph[now]:
            if next_node not in visited:
                q.append(next_node)
                visited[next_node] = visited[now] + 1
                
    
    return 0