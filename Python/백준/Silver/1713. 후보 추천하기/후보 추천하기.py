n = int(input())
l = int(input())
f = []
li = list(map(int, (input().split())))

for i in range(l):
    t = li[i]
    #f는 프레임 이중 리스트로 [추천수, 들어온 순서, 번호]
    st_li = [info[2] for info in f]
    if t in st_li:
        idx = st_li.index(t)
        f[idx][0]+=1
    else:
        if len(f) == n:
            f.sort(key = lambda x: [x[0],x[1],x[2]])
            f.pop(0)
        f.append([1,i,t])
    #
num_li = [info[2] for info in f]
num_li.sort()
print(*num_li)