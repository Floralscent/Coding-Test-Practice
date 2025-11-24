# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
T = 10 ; n = 100
for _ in range(1, T + 1):
    #
    t = int(input())
    arr = [] 
    for _ in range(100):
        arr.append(list(map(int, (input().split()))))
    #
    ans = []
    arr_t = list(map(list, zip(*arr)))
    
    for lst in arr:
        ans.append(sum(lst))
    for lst in arr_t:
        ans.append(sum(lst))
    cnt_1 = 0 ; cnt_2 = 0
    for i in range(n):
        for j in range(n):
            if i-j ==0:
                cnt_1 += arr[i][j]
            if i+j == n-1:
                cnt_2 += arr[i][j]
    ans.append(cnt_1)
    ans.append(cnt_2)
    
    #
    print(f"#{t} {max(ans)}")