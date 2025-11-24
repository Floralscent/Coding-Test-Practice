T = int(input())

def rsp(s,e):
    a = li[s] ; b =li[e]
    if a == b:
        return s if s <e else e
    elif (a ==1 and b==3) or (a==2 and b ==1) or (a==3 and b==2):
        return s
    else:
        return e
    
def to(s,e):
    if s== e:
        return s
    mid = (s+e)//2
    left = to(s,mid)
    right = to(mid+1,e)
    return rsp(left,right)

for test_case in range(1, T + 1):
    # 
    n = int(input())
    li = [0] + list(map(int, (input().split())))
    ans = to(1,n)
    print(f"#{test_case} {ans}")