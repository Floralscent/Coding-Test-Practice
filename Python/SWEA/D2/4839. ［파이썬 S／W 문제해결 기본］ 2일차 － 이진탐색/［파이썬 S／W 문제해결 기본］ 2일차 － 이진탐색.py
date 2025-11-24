T = int(input())

def finding(p,t):
    cnt = 0
    l = 1; r = p
    
    while True: #l <=r:
        c = (l+r)//2
        cnt+=1
        if c == t:
            return cnt
        elif c <t:
            l = c
        else:
            r = c



# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 
    p,a,b = map(int, (input().split()))
    
    cnt_a = finding(p,a)
    cnt_b = finding(p,b)
    
    if cnt_a == cnt_b :
        ans = 0
    elif cnt_a > cnt_b:
        ans = "B"
    else:
        ans = "A"
    print(f"#{test_case} {ans}")