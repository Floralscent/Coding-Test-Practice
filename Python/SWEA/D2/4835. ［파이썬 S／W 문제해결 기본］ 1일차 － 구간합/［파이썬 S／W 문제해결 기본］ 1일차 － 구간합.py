t= int(input())
for q in range(1,t+1):
    n,m = map(int, input().split())
    li = list(map(int, input().split()))
    
    win = li[:m]
    win = sum(win)
    near_max = near_min = win
    for i in range(n-m):
        win = win -li[i]+li[i+m]
        near_max = max(win,near_max)
        near_min = min(win,near_min)
    print("#"+str(q), near_max-near_min)