import heapq

def solution(n, paths, gates, summits):
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    # 1단계: 변수 이름 변경
    intensity = [INF] * (n + 1)
    
    # set으로 변환하여 탐색 속도 향상
    summits_set = set(summits)

    for st, ed, co in paths:
        graph[st].append((co, ed))
        graph[ed].append((co, st))

    def dijkstra():
        q = []
        
        # 3단계: 모든 출입구를 동시 출발점으로 설정
        for gate in gates:
            heapq.heappush(q, (0, gate))
            intensity[gate] = 0

        while q:
            current_intensity, now = heapq.heappop(q)
            
            # 현재 경로의 intensity가 이미 기록된 최소 intensity보다 크면 무시
            if current_intensity > intensity[now]:
                continue
            
            # 현재 위치가 산봉우리이면 더 이상 탐색하지 않음 (규칙)
            if now in summits_set:
                continue

            for weight, next_node in graph[now]:
                # 2단계: 비용(intensity) 계산 로직 변경
                new_intensity = max(current_intensity, weight)
                
                if new_intensity < intensity[next_node]:
                    intensity[next_node] = new_intensity
                    heapq.heappush(q, (new_intensity, next_node))
    
    dijkstra()
    
    # 4단계: 최종 정답 찾기
    answer = [-1, INF] # [산봉우리 번호, 최소 intensity]
    
    # 산봉우리를 번호 순으로 정렬하여 확인 (intensity가 같을 때 번호가 작은 것을 선택하기 위함)
    summits.sort()
    
    for summit in summits:
        if intensity[summit] < answer[1]:
            answer[0] = summit
            answer[1] = intensity[summit]
            
    return answer