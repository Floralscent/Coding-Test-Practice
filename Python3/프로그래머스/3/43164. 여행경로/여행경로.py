
from collections import defaultdict

def solution(tickets):
    # 
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    #
    for key in graph:
        graph[key].sort()

    stack = ["ICN"]
    path = [] # 최종 경로를 담을 리스트

    # 
    while stack:
        now = stack[-1]

        # 
        if graph[now]:
            # 
            d = graph[now].pop(0)
            stack.append(d)
        # 
        else:
            path.append(stack.pop())

    return path[::-1]