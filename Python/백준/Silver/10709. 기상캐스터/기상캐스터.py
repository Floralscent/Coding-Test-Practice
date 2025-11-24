import sys

n,m =map(int, input().split())
ans = []
idx = -1

for i in range(n):
    tmp = list(sys.stdin.readline().strip())
    tmp_idx = -1
    for j in range(m):
        if tmp_idx == -1: #c를 발견한적 없음
            if tmp[j] == ".": #c를 발견한적 없으며 본인도 c가 아님
                tmp[j] = idx
            else:
                tmp_idx = 0; tmp[j] = 0 #c를 발견한적 없으나 본인이 c임
        else:
            if tmp[j] == ".": #c를 발견한적 있으나 본인이 c가 아님
                    tmp_idx += 1
                    tmp[j] = tmp_idx
            else: # c를 발견했고 본인도 c임
                tmp_idx = 0; tmp[j] = 0
    ans.append(tmp)
    print(*ans[i])
            