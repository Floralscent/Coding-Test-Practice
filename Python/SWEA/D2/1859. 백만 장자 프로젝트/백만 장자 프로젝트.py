t = int(input())
for q in range(1, t + 1):
    n = int(input())
    li = list(map(int, input().split()))
    max_val = li[-1]
    cnt = 0
    for i in range(n - 1, -1, -1):  # 뒤에서부터 앞으로
        if li[i] > max_val:
            max_val = li[i]
        else:
            cnt += (max_val - li[i])
    print("#" + str(q), cnt)
