T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 
    li = []
    wd =input()
    ans = 1
    for i in range(len(wd)):
        if wd[i] == "{" or wd[i] =="(":
            li.append(wd[i])
        elif wd[i] == "}" :
            if li:
                tmp = li.pop()
                if tmp == "{":
                    pass
                else: 
                    ans = 0
            else:
                ans = 0
        elif wd[i] == ")":
            if li:
                tmp = li.pop()
                if tmp == "(":
                    pass
                else: 
                    ans = 0
            else:
                ans = 0
    #
    if li:
        ans =0
    
    print(f"#{test_case} {ans}")
            