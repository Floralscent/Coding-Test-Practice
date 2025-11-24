def solution(sticker):
    n = len(sticker)

    # 스티커가 1개인 경우 > 바로 반환
    if n == 1:
        return sticker[0]
    
    # 1번(idx = 0)처음을 선택한 경우, n번 (idx = n-1)x
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    
    for i in range(2, n - 1):  # 마지막 스티커를 제외
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    # 2번 (idx = 1) 선택 경우 , n번 가능 ㅇ
    dp2 = [0] * n
    dp2[1] = sticker[1]
    
    for i in range(2, n):  # 첫 번째 스티커를 제외
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])
        
    return max(dp1[n - 2], dp2[n - 1])