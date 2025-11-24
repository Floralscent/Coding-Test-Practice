import sys

input = sys.stdin.readline
n,k = map(int, (input().split()))

li = []
lst = list(map(int, (input().split())))

if n>=k:
    print(0)
    exit(0)

count = 0
for i in range(k):
    
    if lst[i] in li:
        continue
        # print("이미 있으니 유지",lst[i])

    if len(li) < n:
        li.append(lst[i])
        continue

    tmp = []
    for num in li:
        try:
            idx = lst.index(num,i)
        except:
            idx = k+1            
        tmp.append((idx,num))
    tmp.sort(reverse = True)        # tmp[0][1] << # 얘가 교체될 아이, 숫자임
    idx = li.index(tmp[0][1])
    li[idx] = lst[i]        
    count+=1
        # print(" 로 교체",lst[i])
# print("###########")        
print(count)