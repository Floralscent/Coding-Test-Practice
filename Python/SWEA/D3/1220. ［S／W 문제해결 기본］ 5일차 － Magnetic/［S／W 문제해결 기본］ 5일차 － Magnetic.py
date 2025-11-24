
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    ans = 0
    for _ in range(n):
        arr.append(list(map(int, (input().split()))))
    #
    
    for j in range(n):
        li = [arr[i][j] for i in range(n)]
        flag = False
        for k in range(n):
            if li[k] == 1 and flag == False:
                flag = True
            elif li[k] == 2 and flag == True:
                ans+=1
                flag = False
        
        '''이건 남은 돌맹이 숫자
        li_tmp = li[::-1]
        ###
        try:
            idx_1 = li.index(1)
        except:
            idx_1 = 100
        ###
        try:
            idx_2 = len(li) - li_tmp.index(2) -1
        except:
            idx_2 = 0
         #
        
        for k in range(n):
            if li[k] ==2 and k<idx_1:
                li[k] = 0
            elif li[k] == 1 and k>idx_2:
                li[k] = 0
        #
        ans += (li.count(1)+li.count(2))
        '''
    print(f"#{test_case} {ans}")