h, n = map(int, input().split())

li = [0]+list(map(int, input().split()))+[0]

left_hi = 0; right_hi =0 ; cnt = 0
for i in range(1,n+1):
    
    left_hi = max(li[:i]) ;  right_hi = max(li[i+1:])
    w_hi = min(left_hi, right_hi)
    if w_hi > li[i]:
        cnt += (w_hi - li[i])
        # print(cnt)
    
print(cnt)