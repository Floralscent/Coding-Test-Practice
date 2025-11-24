def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
        
    '''
    1,2,3,4,5 들어왔을때
    i = 0, 끝, stack이 비워있음으로 1은 그냥 들어감
    i = 1, stack[-1][1] = 1, prices[i]=2이므로 걍 추가
    i = 2, stack[-1][1] = 2, prices[i]=3이므로 걍 추가
    i = 3, stack[-1][1] = 3, prices[i]=2이므로
    past = 2 > answer[2] = 3-2 = 1 stack에 3,2 넣음
    i = 4, stack[-1][1] = 2, prices[i]=3이므로 걍 추가
    stack = [[0,1], [1,2], >[2,3]< , [3,2],[4,3] ]
    answer = [0,0,1,0,0]
    '''
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer