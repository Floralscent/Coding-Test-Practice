r,c = map(int, (input().split()))
graph =[]; idx = []
change_arr = []

for i in range(r):
    wd = list(input())
    id = [(i,j) for j in range(len(wd)) if wd[j] == "X"]
    graph.append(wd)
    idx +=id
#

def chk(i,j):
    dx = [-1,1,0,0]; dy = [0,0,-1,1]
    ch = [0,0,0,0] # 상하좌우 체크 배열 , 0이 X 1이 .
    for k in range(4):
        nx = i+dx[k]; ny =j+dy[k]

        if 0<=nx<r and 0<=ny<c:
            if graph[nx][ny] ==".":
                ch[k] = 1
        else:
            ch[k]=1
    cnt = ch.count(1)
    if cnt >= 3:
        change_arr.append((i,j))

for idx1,idx2 in idx:
    chk(idx1,idx2)

for x,y in change_arr:
    graph[x][y] = "."
#print(*idx)

an = []; mi_idx = c; mx_idx=0
up_idx = r+1; lo_idx = 0

for q in range(r):
    ans = "".join(graph[q])
    
    if "X" in ans:
        mi_idx = min(ans.index("X"),mi_idx)
        mx_idx = max(ans.rindex("X"),mx_idx)
        lo_idx = max(q,lo_idx)
        up_idx = min(q,up_idx)

    an.append(ans)
    
an = an[up_idx:lo_idx+1]
for o in an:
    print(o[mi_idx:mx_idx+1])
