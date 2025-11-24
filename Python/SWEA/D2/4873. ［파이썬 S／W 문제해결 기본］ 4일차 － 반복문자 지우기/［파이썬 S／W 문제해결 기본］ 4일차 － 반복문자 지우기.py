T = int(input())
for test_case in range(1, T + 1):
    # 
    li = list(input())
    tmp = []
    for i in range(len(li)):
        if i == 0:
            tmp.append(li[i])
            continue
        #
        if tmp and li[i] == tmp[-1]:
            tmp.pop()
            #
        else:
            tmp.append(li[i])
        
    #
    ans = len(tmp)
    #print(*tmp)
    print(f"#{test_case} {ans}")