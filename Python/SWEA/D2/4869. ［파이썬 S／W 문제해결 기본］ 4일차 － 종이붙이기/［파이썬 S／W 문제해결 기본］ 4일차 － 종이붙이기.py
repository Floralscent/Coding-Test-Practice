T = int(input())
for test_case in range(1, T + 1):
    #
    n = int(input())
    n = n//10
    d= [0] * (n+1)
    d[1] = 1; d[2]=3
    for i in range(1,n+1):
        if i==1 or i ==2:
            pass
        else:
            d[i] = d[i-1]+d[i-2]*2
    ans = d[n]
    print(f"#{test_case} {ans}")