import sys
from collections import deque

# sys.stdin = open("input.txt", "r")


# bfs
def bfs(si,sj):
    # 1 q, v, 필요 자료형 생성
    q = deque()
    v = [[0]*n for _ in range(n)]
    tlist = []

    #2 q에 초기 데이터들 삽입, v 표시
    q.append((si,sj))
    v[si][sj] = 1 # 처음 자리는 아기 상어 위치며 방문처리
    dist = 0
    di = [-1,1,0,0] ; dj = [0, 0, -1, 1]
    # 4 방향 /범위내 / 미방문/ 조건
    while q:
        ci, cj = q.popleft()
        if dist == v[ci][cj]:
            return tlist, dist-1
         
        for i in range(4):
            ni = ci + di[i]
            nj = cj + dj[i]

            if 0<=ni<n and 0<=nj<n and v[ni][nj] == 0 and arr[ni][nj] <= shark:
                q.append((ni,nj)) # 방문
                v[ni][nj] = v[ci][cj] + 1 # 거리는 이전꺼 보다 하나 증가

                # 나보다 작은 물고기일때만 tlist에 추가
                if shark > arr[ni][nj] >0 :
                    tlist.append((ni,nj))
                    dist = v[ni][nj] 
    
    # q가 비어있을 경우, 방문이 끝났을때
    return tlist , dist-1 #거리에서 1빼주는 이유는 방문 처리 1이 디폴트



# 입력 파트
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int,input().rstrip().split())) for _ in range(n)] 

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9: #아기상어 위치 파악
            ci, cj = i,j
            arr[i][j] = 0

# 초기화
shark = 2; cnt = ans = 0

while True:
    tlist, dist = bfs(ci,cj) # 먹을 수 있는 물고기 목록, 거리
    if len(tlist) == 0:
        break

    tlist.sort(key = lambda x : (x[0],x[1])) # 행/열 정렬
    ci, cj = tlist[0] # 다음 bfs의 좌표 갱신
    arr[ci][cj] = 0  # 물고기 먹기
    cnt +=1; ans +=dist
    if shark ==cnt:
        shark +=1
        cnt = 0


print(ans)