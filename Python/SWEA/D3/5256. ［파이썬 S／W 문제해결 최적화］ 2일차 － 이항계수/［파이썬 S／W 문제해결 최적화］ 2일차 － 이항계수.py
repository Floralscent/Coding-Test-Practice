T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def fac(x):
    if x ==1:
        return 1
    ans = 1
    for i in range(2,x+1):
        ans *= i
    return ans

def com(n,r):
    return fac(n) // (fac(n-r) * fac(r))

for test_case in range(1, T + 1):
    # 
    n,a,b = map(int, (input().split()))
    ans = com(n,a)
    print(f"#{test_case} {ans}")