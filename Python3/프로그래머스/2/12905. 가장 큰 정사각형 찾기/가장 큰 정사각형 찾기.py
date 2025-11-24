def solution(board):
    n = len(board)  # row (행)
    m = len(board[0])  # col (열)

    # dp 배열을 0으로 초기화 (n x m 크기의 2차원 배열 생성)
    dp = [[0] * m for _ in range(n)]
    
    # 첫 번째 행과 첫 번째 열 초기화
    for i in range(n):
        dp[i][0] = board[i][0]  # 첫 번째 열
    for j in range(m):
        dp[0][j] = board[0][j]  # 첫 번째 행
        
    # DP 배열 채우기
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    # 최대 정사각형의 한 변의 길이 찾기
    max_square_length = 0
    for i in range(n):
        max_square_length = max(max_square_length, max(dp[i]))
    
    # 정사각형의 넓이 = 한 변의 길이의 제곱
    return max_square_length ** 2
