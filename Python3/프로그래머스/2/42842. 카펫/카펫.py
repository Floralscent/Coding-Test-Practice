def solution(brown, yellow):
    # 총 타일의 개수는 brown + yellow
    total_tiles = brown + yellow
    
    # row와 col은 최소 3 이상이므로 3부터 시작
    for row in range(3, total_tiles // 3 + 1):  
        if total_tiles % row == 0:
            col = total_tiles // row
            # row가 b, col이 y라고 할 때, 위 공식에 맞는지 확인
            if (row - 2) * (col - 2) == yellow:
                return [row, col] if row >= col else [col, row]
