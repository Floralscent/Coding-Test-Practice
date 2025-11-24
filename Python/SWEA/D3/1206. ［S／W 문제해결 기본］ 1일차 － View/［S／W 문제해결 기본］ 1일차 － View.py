for q in range(1,11):
    n = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    for i in range(2,len(li)-2):
        tmp = li[i] ; near_max = max( li[i-2], li[i-1], li[i+1], li[i+2])
        if tmp >near_max:
            cnt += (tmp - near_max)
            # print(i, cnt)
    # print("############3")
    print("#"+str(q),cnt)