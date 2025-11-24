T = 10
for test_case in range(1, T + 1):
    #
    l = int(input())
    li = list(map(int, (input().split())))
    p = int(input())
    tmp_p_li = input().split("I")[1:]
    #print(f"{p_li[0]} {p_li[1]}")
    for i in range(p):
        p_li=list(tmp_p_li[i].split())
        w = int(p_li[0]);  lo = int(p_li[1]) # 위치와 삽입될 갯수
        for j in range(lo):
            idx = w+j
            li.insert(idx, int(p_li[j+2]))
        #
    #li = li[1:]
    ans = " ".join(str(li[j]) for j in range(10))
    '''
    ans = ""
    for j in range(10):
        ans += str(li[j]) + " "

    '''
    print(f"#{test_case} {ans}")