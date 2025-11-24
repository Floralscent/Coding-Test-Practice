T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #
    l,wd = map(str, (input().split()))
    l = int(l)
    li = []

    for i in range(len(wd)):
        if i == 0:
            li.append(wd[0])
        #
        else:
            if li and li[-1] == wd[i]:
                li.pop()
            else:
                li.append(wd[i])
    ##8 231231321
    ans = "".join(map(str, li))
    print(f"#{test_case} {ans}")