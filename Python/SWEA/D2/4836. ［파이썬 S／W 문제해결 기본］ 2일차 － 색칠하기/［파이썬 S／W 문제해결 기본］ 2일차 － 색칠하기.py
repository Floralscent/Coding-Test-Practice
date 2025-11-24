T = int(input())
for test_case in range(1, T + 1):
    # 
    n = int(input())
    arr = [[0] *10 for _ in range(10)]
    for _ in range(n):
        r1,c1,r2,c2,p = map(int, (input().split()))
        #arr[r1][c1] ~ arr[r2][c2] += c
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                arr[r][c] += p
            #
       #
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt+=1
    #print(*arr)
    print(f"#{test_case} {cnt}")