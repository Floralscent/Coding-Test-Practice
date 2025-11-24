T = int(input())
for test_case in range(1, T + 1):
    # 
    N,M = map(int, (input().split()))
    li = [] ; cnt = 0
    for _ in range(N):
        w = input()
        n = len(w)
        tmp = [w[:n-x] for x in range(n)]
        li = li+tmp
    for _ in range(M):
        word= input()
        if word in li:
            cnt+=1
        #
    #
    print(f"#{test_case} {cnt}")