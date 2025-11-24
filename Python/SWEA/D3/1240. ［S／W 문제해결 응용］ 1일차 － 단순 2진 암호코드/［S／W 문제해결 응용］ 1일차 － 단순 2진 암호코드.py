T = int(input())
#table
table = {"0001101":0, "0011001":1, "0010011":2, "0111101":3, "0100011":4, "0110001":5, "0101111":6, "0111011":7, "0110111":8, "0001011":9}
for test_case in range(1, T + 1):
    n , m = map(int, (input().split()))
    li = []
    ans = False
    for _ in range(n):
        code = input()
        if "1" in code:
            li.append(code)
        #
    num = li[0]
    idx = num.rindex("1")
    tmp = li.pop(0)
    # 56 자리로 변경 
    num = tmp[idx-55:idx+1]
    num_li = [0]+[table[num[x:x+7]] for x in range(0,56,7)]
    #print(num_li)
    odd = 0 ; even = 0
    for j in range(len(num_li)): #1이 홀수이자 idx 0 
        if j%2 == 0:
            even += num_li[j]
        else:
            odd += num_li[j]
    check = odd*3 + even
    #print(check)
    if check %10  == 0:
        print(f"#{test_case} {sum(num_li)}")
    else:
        print(f"#{test_case} 0")