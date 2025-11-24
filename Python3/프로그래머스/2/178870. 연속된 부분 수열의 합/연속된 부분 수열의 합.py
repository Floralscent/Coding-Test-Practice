def solution(sequence, k):
    n = len(sequence)
    start, end = 0, 0
    current_sum = sequence[0]
    answer = [(0,n)] 

    while start < n:
        # 합이 k와 같은 경우
        if current_sum == k:
            # 현재 구간의 길이가 기존 answer의 길이보다 짧으면 갱신
            #if (end - start) < (answer[1] - answer[0]):
            answer.append((start, end))
            
            # 다음 탐색을 위해 start를 오른쪽으로 한 칸 이동
            current_sum -= sequence[start]
            start += 1
        
        # 합이 k보다 작은 경우
        elif current_sum < k:
            end += 1
            if end < n:
                current_sum += sequence[end]
            else: # end가 범위를 벗어나면 더 이상 탐색 불가
                break
        
        # 합이 k보다 큰 경우
        else: # current_sum > k
            current_sum -= sequence[start]
            start += 1
    
    answer.sort(key = lambda x: x[1] - x[0])
    return answer[0]