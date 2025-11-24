# Python 풀이
import  sys
input = sys.stdin.readline

n,k  =  map(int,input().split())
arr  =  list(map(int,input().split()))

minus  = []
plus  = []

for  idx  in  range(n):
    if  arr[idx] >  0: # 양수면
        plus.append(arr[idx])

    elif  arr[idx] <  0: # 음수면
        minus.append(-arr[idx]) # 절대값 처리

plus.sort(reverse=True)
minus.sort(reverse=True)

tot = 0

for idx in range(0, len(plus),k):
    tot += plus[idx]*2 # 왕복으로 갔다와야하기 때문에

for idx in range(0, len(minus),k):
    tot += minus[idx]*2 

### 위의 코드는 왕복으로 계산했으나 마지막, 가장 먼 걸이는 돌아올필요 x

if not plus:
    tot -= minus[0] # 마이너스만 있는 경우 가장 먼건 마이너스의 첫번째
elif not minus:
    tot -= plus[0]

else : 
    tot -= max(plus[0],minus[0])

print(tot)