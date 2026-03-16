import sys
input = sys.stdin.readline

n,m = map(int, (input().split()))
li =[]


for _ in range(n):
    wd,num = map(str, (input().split()))
    num = int(num)
    if li and li[-1][0] == num:
        continue
    li.append((wd,num))

li.sort(key = lambda x: (x[1]))

def binary_search(arr,t):

    s = 0 ; e = len(arr)
    
    while s<e:
        mid = (s+e)//2
        if arr[mid][1] < t:
            s = mid+1
        else:
            e = mid
    #
    return e
#
for _ in range(m):
    tmp = int(input())
    idx = binary_search(li, tmp)
    print(li[idx][0])
    
    #