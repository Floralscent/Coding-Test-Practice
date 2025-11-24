T = 10

def check_arr(arr,wd):
    cnt = 0
    for lst in arr:
        for i in range(len(lst)-wd+1):
            li = lst[i:i+wd]
            #tmp_li = sorted(li, reverse = True)
            if li == li[::-1]:
                cnt+=1
    return cnt



for test_case in range(1, T + 1):
    #
    wd =int(input())
    arr = []
    for _ in range(8):
        arr.append(list(map(str, input())))
        
    arr_t =list(map(list, zip(*arr)))
    ans = check_arr(arr,wd)+check_arr(arr_t,wd)
    print(f"#{test_case} {ans}")