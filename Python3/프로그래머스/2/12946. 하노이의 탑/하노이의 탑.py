def hanoi(n, start, end, via, answer):
    if n == 1:
        # 원판 1개를 출발지에서 목표지로 이동
        answer.append([start, end])
        return
    # n-1개의 원판을 출발지에서 보조로 이동
    hanoi(n-1, start, via, end, answer)
    # 가장 큰 원판을 출발지에서 목표로 이동
    answer.append([start, end])
    # n-1개의 원판을 보조에서 목표지로 이동
    hanoi(n-1, via, end, start, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)  # 1: 출발지, 2: 보조, 3: 목표
    return answer
