T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 
    s = []
    wd = list(input().split())
    for i in range(len(wd)):
        if i == len(wd)-1:
            if len(s) == 1:
                ans = s.pop()
                break
            else:
                ans = "error"
                break
        try:
            word = int(wd[i])
            s.append(word)
        except:
            word = wd[i]
            if s and len(s)>=2:
                num_1 = s.pop()
                num_2 = s.pop()
                if word == "+":
                    num = num_2+num_1
                elif word == "-":
                    num = num_2 - num_1
                elif word == "*":
                    num = num_2 * num_1
                elif word == "/":
                    num = num_2 // num_1
                else:
                    ans = "error"
                    break
                s.append(num)
            else:
                ans = "error"
                break
            #
    print(f"#{test_case} {ans}")