def solution(m, n, puddles):
    # DP 테이블 초기화
    d = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 출발점은 항상 1
    d[1][1] = 1

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 출발점은 이미 처리했으므로 건너뛰기
            if (i, j) == (1, 1):
                continue
            # 웅덩이가 있는 경우
            if [j, i] in puddles:  # (열, 행)을 (행, 열)로 확인
                d[i][j] = 0
            else:
                d[i][j] = (d[i - 1][j] + d[i][j - 1]) 

    return d[n][m]% 1000000007
